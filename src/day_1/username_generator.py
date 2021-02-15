# Username Generator


def print_welcome(name: str):
    print(f"Welcome to {name}.")


def get_username() -> str:
    user_color = ask_user_favorite('color')
    user_food = ask_user_favorite('food')
    username = create_username_from(user_color, user_food)

    return username


def ask_user_favorite(item: str) -> str:
    return input(f"What's your favorite {item}?\n")


def create_username_from(*args: str):
    if not args:
        raise ValueError("Cant create an empty username")

    username_parts = []
    username_number = 0

    for arg in args:
        username_parts.append(title_string_and_replace_spaces(arg, '-'))
        username_number += len(arg)

    username_number *= len(args)

    username_parts.append(str(username_number))
    username = format_username(username_parts)

    return username


def title_string_and_replace_spaces(string: str, replacement: str):
    result = string.replace(" ", replacement)
    return result.title()


def format_username(username_parts):
    username = f"{'-'.join(username_parts[:-1])}{username_parts[-1]}"
    return username


def main():
    print_welcome("to the username generator")
    username = get_username()

    print(f"Your new username is {username}")


if __name__ == "__main__":
    main()