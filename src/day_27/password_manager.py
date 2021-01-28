import os
import tkinter as tk
import tkinter.messagebox as messagebox

from tkinter import PhotoImage, Tk, Canvas
from PIL import Image, ImageTk
from password_generator import PasswordGenerator

PASSWORD_IMAGE_PATH = os.path.join(os.getcwd(), 'src/day_27/images/pass.png')
PASSWORDS_DATA_FILE_PATH = os.path.join(os.getcwd(),
                                        'src/day_27/data/passwords.txt')


class PasswordManager(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=200, height=150)
        self.website = None
        self.email = None
        self.password = None
        self.password_entry = None
        self.entries = []
        self.passwords_data = []
        self.password_generator = PasswordGenerator()
        self.config_app()
        self.mainloop()

    def generate_password(self):
        self.password_entry.delete(0, tk.END)
        password = self.password_generator.generate_password()
        self.password_entry.insert(0, string=password)
        return password

    def ask_user_to_save_current_data(self):
        try:
            website, email, password = self.passwords_data
            assert website and email and password
        except (AssertionError):
            messagebox.showerror(title="Error",
                                 message='Some fields are empty!')
            return
        else:
            is_ok = messagebox.askokcancel(
                title="Save",
                message=
                f"Website: {website}\nEmail: {email}\nPassword: {password}\n\nDo you want to save?"
            )
            return is_ok

    def delete_entry_inputs(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def click_submit_button(self):
        self.append_data_to_passwords_data()
        if self.ask_user_to_save_current_data():
            self.append_passwords_data_to_file()
            self.delete_entry_inputs()

        self.passwords_data.clear()

    def append_passwords_data_to_file(self):

        with open(PASSWORDS_DATA_FILE_PATH, 'a') as password_data_file:
            password_data_file.write('\n')
            website, email, password = self.passwords_data
            password_data_file.write(
                f"Website: {website}\nEmail: {email}\nPassword: {password}")

            self.write_line_to_file(password_data_file)

    def write_line_to_file(self, filename):
        filename.write('\n')
        filename.write('-' * 20)
        filename.write('\n')

    def append_data_to_passwords_data(self):
        for entry in self.entries:
            data = entry.get()
            self.passwords_data.append(data)

    def config_app(self):
        self.set_screen()
        self.add_password_image()
        self.add_labels()
        self.add_text_areas()
        self.add_buttons()

    def add_labels(self):
        website_label = tk.Label(text='Website:', bg='white')
        website_label.grid(row=1, column=0)

        email_label = tk.Label(text='Email:', bg='white')
        email_label.grid(row=2, column=0, padx=0)

        password_label = tk.Label(text='Password:', bg='white')
        password_label.grid(row=3, column=0)

    def add_text_areas(self):
        website_entry = tk.Entry()
        website_entry.focus()
        website_entry.insert(0, 'https://www.google.com/')
        website_entry.grid(row=1, column=1)

        email_entry = tk.Entry()
        email_entry.insert(0, 'test@gmail.com')
        email_entry.grid(row=2, column=1)

        self.password_entry = tk.Entry()
        self.password_entry.grid(row=3, column=1)

        self.entries.extend([website_entry, email_entry, self.password_entry])

    def add_buttons(self):
        submit_button = tk.Button(text="Submit",
                                  borderwidth=1,
                                  command=self.click_submit_button)
        submit_button.grid(row=4, column=1, pady=20)

        generate_password = tk.Button(text="Generate Password",
                                      borderwidth=1,
                                      command=self.generate_password)
        generate_password.grid(row=4, column=0, pady=20)

    def add_password_image(self):
        image = Image.open(PASSWORD_IMAGE_PATH)
        image = image.resize((150, 150), Image.ANTIALIAS)
        self.password_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(100, 80, image=self.password_image)
        self.canvas.config(bg='white', borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=1, pady=20)

    def set_screen(self):
        self.title(f"Password Manager")
        self.config(padx=20, pady=20, background='#FFF')
        self.geometry('500x400')
        self.resizable(width=False, height=False)


def main():
    pm = PasswordManager()


if __name__ == "__main__":
    main()