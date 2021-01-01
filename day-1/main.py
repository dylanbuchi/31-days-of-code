def print_welcome():
    print("Welcome to the username generator.")


def get_username():
    user_color = input("What's your favorite color?\n")
    user_food = input("What's your favorite food?\n")
    username = create_username(user_color, user_food)

    return f"Your username is {username}"


def create_username(color, food):
    food = food.replace(" ", '-').title()
    color = color.replace(" ", '-').title()
    number = len(color) * len(food)

    return f"{color}-{food}{number}"


def main():
    print_welcome()
    username = get_username()
    print(username)


if __name__ == "__main__":
    main()