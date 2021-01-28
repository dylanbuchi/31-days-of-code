import pyttsx3 as text_to_speech

from tkinter import Button, Canvas, Label, Tk, PhotoImage
from tkinter.constants import LEFT, TOP

from pomodoro_settings import PomodoroAppSettings


class PomodoroTimerApp(Tk):
    def __init__(self):
        super().__init__()
        self.repetition_number = 0
        self.clicked_started_button_count = 0
        self.timer_count = None
        self.settings = PomodoroAppSettings()
        self.tomato_image = PhotoImage(file=self.settings.TOMATO_IMAGE_PATH)
        self.work_break_label = Label(text='',
                                      fg=self.settings.GREEN,
                                      bg=self.settings.LIGHT_RED,
                                      font=self.settings.WORK_BREAK_LABEL)
        self.work_break_label.pack(side=TOP, pady=0)

        self.canvas = Canvas(width=600, height=600)
        self.setup_text_to_speech()
        self.setup_pomodoro_screen()
        self.setup_canvas_screen()
        self.timer_label = self.add_timer_label_for_canvas(
            300, 330, text='25:00', fill='#FFF', font=self.settings.TIMER_FONT)
        self.setup_buttons()

    def setup_text_to_speech(self):
        self.engine = text_to_speech.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def click_start_button(self):
        # break out if user clicks the start button multiples times
        if self.clicked_started_button_count == 1:
            return
        self.clicked_started_button_count += 1

        self.start_timer()

    def setup_buttons(self):
        self.add_start_button()
        self.add_reset_button()

    def add_start_button(self):
        button = Button(self,
                        text="Start",
                        borderwidth=0,
                        activeforeground=self.settings.LIGHT_RED,
                        background='white',
                        font=self.settings.START_BUTTON_FONT,
                        command=self.click_start_button)
        button.pack(side=LEFT, padx=100)

    def add_reset_button(self):
        button = Button(self,
                        text="Reset",
                        borderwidth=0,
                        activeforeground=self.settings.LIGHT_RED,
                        background='white',
                        font=self.settings.START_BUTTON_FONT,
                        command=self.reset_timer)
        button.pack(side=TOP)

    def setup_pomodoro_screen(self):
        width = self.winfo_screenwidth()
        add_spaces = (" " * (int(width) // 50))

        self.title(f"{add_spaces}Big Pomodoro Timer")
        self.config(padx=100, pady=50, background='#F6CFCF')
        self.resizable(width=False, height=False)

    def reset_timer(self):
        if self.timer_count:
            self.after_cancel(self.timer_count)

        self.canvas.itemconfigure(self.timer_label, text="25:00")
        self.work_break_label.config(text="")

        self.repetition_number = 0
        self.clicked_started_button_count = 0
        self.timer_count = None

    def start_timer(self):
        self.repetition_number += 1
        rep_num = self.repetition_number

        # long break of 25 min
        if rep_num % 8 == 0:
            text = "It's time for a big break!"
            self.work_break_label.config(text="It's time for a big break!",
                                         fg=self.settings.RED)
            self.count_down(self.settings.LONG_BREAK_MINUTES)
            text_to_speech.speak(text)

        # short break 5 min
        elif rep_num % 2 == 0:
            text = "It's time for a break!"
            self.work_break_label.config(text=text, fg=self.settings.RED)
            self.count_down(self.settings.SHORT_BREAK_MINUTES)
            text_to_speech.speak(text)
        else:
            # work time
            text = "It's time to work!"
            text_to_speech.speak(text)
            self.work_break_label.config(text=text, fg=self.settings.GREEN)
            self.count_down(self.settings.WORK_MINUTES)

    def count_down(self, count):
        if count == -1:
            self.start_timer()
        else:
            minutes = count // 60
            seconds = count % 60

            if count < 10:
                seconds = f"0{seconds}"
            elif int(seconds) < 10:
                seconds = f"0{seconds}"

            timer = f"{minutes}:{seconds}"

            self.canvas.itemconfigure(self.timer_label, text=timer)
            self.timer_count = self.after(1000, self.count_down, count - 1)

    def setup_canvas_screen(self):
        self.canvas.config(background=self.settings.LIGHT_RED,
                           highlightthickness=0)
        self.pack_items_to_canvas()

    def pack_items_to_canvas(self):
        self.add_tomato_image_to_canvas()
        self.canvas.pack()

    def add_timer_label_for_canvas(self, x, y, text, fill, font):
        return self.canvas.create_text(x, y, text=text, fill=fill, font=font)

    def kill_app(self):
        self.destroy()

    def add_tomato_image_to_canvas(self):
        self.canvas.create_image(300, 300, image=self.tomato_image)
