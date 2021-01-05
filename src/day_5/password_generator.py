import random

#Password Generator


def generate_password(nb_letters, nb_symbols, nb_numbers):
    lower_letters_list = [chr(i) for i in range(97, 123)]
    letters_list = [i.upper() for i in lower_letters_list] + lower_letters_list

    numbers_list = [i for i in range(10)]
    symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '.', '-', '=']

    return get_password(nb_letters, nb_symbols, nb_numbers, letters_list,
                        numbers_list, symbols_list)


def get_password(*args):
    nb_letters, nb_symbols, nb_numbers, letters_list, numbers_list, symbols_list = args
    password = []

    append_character_to_password(nb_letters, letters_list, password)
    append_character_to_password(nb_symbols, symbols_list, password)
    append_character_to_password(nb_numbers, numbers_list, password)

    random.shuffle(password)
    return ''.join(password)


def append_character_to_password(user_number, lst, password):
    for _ in range(user_number):
        ch = random.choice(lst)
        password.append(str(ch))


def main():
    print("Welcome to BIGSECURE Password Generator!!")

    letters, symbols, numbers = ask_user_password_details()

    print("Here is your new password: ")
    print(generate_password(letters, symbols, numbers))


def ask_user_password_details():
    while True:
        try:
            nb_letters = int(
                input("How many letters would you like in your password?\n"))
            assert nb_letters > 0

            nb_symbols = int(input(f"How many symbols would you like?\n"))
            assert nb_symbols > 0

            nb_numbers = int(input(f"How many numbers would you like?\n"))
            assert nb_numbers > 0

        except (ValueError, AssertionError):
            print("Please enter a valid numbers")
            continue
        else:
            break

    return nb_letters, nb_symbols, nb_numbers


if __name__ == "__main__":
    main()