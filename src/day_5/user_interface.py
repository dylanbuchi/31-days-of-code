from password_generator import PasswordGenerator


class UserInterface():
    def __init__(self):
        self.nb_letters = self.nb_symbols = self.nb_numbers = None

    def print_welcome(self):
        print("Welcome to BIGSECURE Password Generator!!")

    def ask_user_password_details(self):
        while True:
            try:
                self.nb_letters = int(
                    input(
                        "How many letters would you like in your password?\n"))
                assert self.nb_letters > 0

                self.nb_symbols = int(
                    input(f"How many symbols would you like?\n"))
                assert self.nb_symbols > 0

                self.nb_numbers = int(
                    input(f"How many numbers would you like?\n"))
                assert self.nb_numbers > 0

            except (ValueError, AssertionError):
                print("Please enter a valid number")
                continue
            else:
                break

    def generate_password(self):
        password = PasswordGenerator(self.nb_letters, self.nb_symbols,
                                     self.nb_numbers).generate_password()
        return password

    def run(self):
        self.print_welcome()
        self.ask_user_password_details()

        print("Here is your new password: ")
        print(self.generate_password())


def main():
    ui = UserInterface()
    ui.run()


if __name__ == "__main__":
    main()