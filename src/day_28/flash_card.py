import os
import sys
import pandas
import random
import tkinter as tk

CSV_FRENCH_WORDS_FILE_PATH = os.path.join(os.getcwd(),
                                          "src/day_28/data/french_words.csv")
IMAGES_PATH = os.path.join(os.getcwd(), "src/day_28/images/")

FLASHCARD_IMAGE_PATH = f"{IMAGES_PATH}flash_card.png"
BACK_FLASHCARD_IMAGE_PATH = f"{IMAGES_PATH}back_flash_card.png"

WRONG_IMAGE_PATH = f"{IMAGES_PATH}wrong.png"
RIGHT_IMAGE_PATH = f"{IMAGES_PATH}right.png"

BG_COLOR = '#a4dea0'
FONT_NAME = 'MonoLisa-Medium'
FONT_NAME_ITALIC = 'MonoLisa-MediumItalic'


class Flashcard(tk.Tk):
    def __init__(self):
        super().__init__()
        # fields
        self.french_word = None
        self.english_word = None
        self.card_title = None
        self.card_word = None

        self.change_card_canvas_image = None

        self.french_english_words_dict = pandas.read_csv(
            CSV_FRENCH_WORDS_FILE_PATH).to_dict(orient='records')
        self.right_or_wrong_button_is_clicked = False
        self.clicked_on_canvas_image = False
        self.canvas = tk.Canvas(width=700, height=500)
        # images
        self.flash_card_image = tk.PhotoImage(file=f"{FLASHCARD_IMAGE_PATH}")
        self.back_flash_card_image = tk.PhotoImage(
            file=f"{BACK_FLASHCARD_IMAGE_PATH}")
        self.wrong_card_image = tk.PhotoImage(file=f"{WRONG_IMAGE_PATH}")
        self.right_card_image = tk.PhotoImage(file=f"{RIGHT_IMAGE_PATH}")
        # methods
        self.config_app_screen()
        self.add_flash_card_image_to_canvas()
        self.add_words_to_canvas()
        self.add_right_and_wrong_buttons()
        self.mainloop()

    def get_random_flashcard(self) -> dict:
        """get a random list of dicts: {French: word, English: word} and return it"""
        try:
            return random.choice(self.french_english_words_dict)
        except IndexError:
            sys.exit()

    def remove_known_card_from_french_english_words_dict(self):
        temp = self.french_english_words_dict[:]
        index = next((index for (index, dic) in enumerate(temp)
                      if dic["French"] == self.french_word.lower()), None)
        if temp:
            temp.pop(index)
        else:
            sys.exit()
        self.french_english_words_dict = temp

    def click_right_button(self):
        self.right_or_wrong_button_is_clicked = True
        self.store_card_words()
        self.remove_from_known_card_from_french_english_words_dict()
        self.add_flashcard_to_canvas()

    def click_wrong_button(self):
        self.right_or_wrong_button_is_clicked = True
        self.store_card_words()
        self.add_flashcard_to_canvas()

    def click_on_canvas_image(self, event):
        self.clicked_on_canvas_image = True
        self.add_flashcard_to_canvas()

    def store_card_words(self):
        flash_card = self.get_random_flashcard()
        french_card_word = flash_card['French'].title()
        english_card_word = flash_card['English'].title()
        self.french_word = french_card_word
        self.english_word = english_card_word

    def add_flashcard_to_canvas(self):
        if self.right_or_wrong_button_is_clicked:
            self.canvas.itemconfig(self.card_title,
                                   text='French',
                                   fill='black')
            self.canvas.itemconfig(self.card_word,
                                   text=self.french_word,
                                   fill='black')

            self.config_canvas_french_card()
            self.right_or_wrong_button_is_clicked = False

        elif self.clicked_on_canvas_image:
            self.canvas.itemconfig(self.card_title,
                                   text='English',
                                   fill='white')
            self.canvas.itemconfig(self.card_word,
                                   text=self.english_word,
                                   fill='white')
            self.config_canvas_english_card()
            self.clicked_on_canvas_image = False

    def config_canvas_french_card(self):
        self.canvas.itemconfigure(self.change_card_canvas_image,
                                  image=self.flash_card_image)

    def config_canvas_english_card(self):
        self.canvas.itemconfigure(self.change_card_canvas_image,
                                  image=self.back_flash_card_image)

    def config_app_screen(self):
        space = ' ' * 25
        self.title(f"Flashcards { space} French - English  ")
        self.config(padx=50, pady=70, background=BG_COLOR)
        self.geometry('800x800')
        self.resizable(width=False, height=False)

    def add_flash_card_image_to_canvas(self):
        self.change_card_canvas_image = self.canvas.create_image(
            350, 250, image=self.flash_card_image)
        self.canvas.bind("<Button-1>", self.click_on_canvas_image)
        self.canvas.config(bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack()

    def add_words_to_canvas(self):
        # Title
        cards = self.get_random_flashcard()

        french_word = cards["French"]
        english_word = cards["English"]

        self.french_word = french_word
        self.english_word = english_word

        self.card_title = self.canvas.create_text(350,
                                                  165,
                                                  text="French",
                                                  font=(FONT_NAME_ITALIC, 18))
        # Word
        self.card_word = self.canvas.create_text(350,
                                                 295,
                                                 text=french_word,
                                                 font=(FONT_NAME, 30, 'bold'))

    def add_right_and_wrong_buttons(self):
        # Right button
        right_button = tk.Button(image=self.right_card_image,
                                 highlightthickness=0,
                                 command=self.click_right_button)
        right_button.pack(side=tk.RIGHT, padx=100, pady=(50, 0))

        # Wrong button
        wrong_button = tk.Button(image=self.wrong_card_image,
                                 highlightthickness=0,
                                 command=self.click_wrong_button)
        wrong_button.pack(side=tk.LEFT, padx=100, pady=(50, 0))
