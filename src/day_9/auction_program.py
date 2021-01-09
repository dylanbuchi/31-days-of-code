# Auction_Program
import os
import sys
import re
# add to path for imports to work
sys.path.append(os.path.join(os.getcwd(), 'src', 'day_9'))

from logo import LOGO


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_welcome_message():
    return "Welcome to my auction program"


def get_user_name(names):
    try:
        name = input("What's your name?\n").title().strip()
        if check_user_name(name, names):
            print(
                "This name is already in our database. Please choose an username"
            )
            return get_user_name(names)

        assert re.match(r"^[a-z A-Z]+$", name) != None

    except AssertionError:
        print("Please enter a valid name")
        return get_user_name(names)

    else:
        return name


def get_user_bid_amount():
    try:
        bid = int(input("What's your bid?\n$").strip())
        assert bid > 0

    except (ValueError, AssertionError):
        # recursive calls until user enters a valid input
        print('Please enter a valid amount')
        return get_user_bid_amount()

    else:
        return bid


def ask_user_more_biders():
    try:
        answer = input("Are there any other bidders? (y/n)\n").lower().strip()
        assert answer == 'y' or answer == 'n'
    except AssertionError:
        print("Please enter 'y' or 'n'")
        return ask_user_more_biders()
    else:
        return answer


def get_winner(name_bid_amount):
    max_amount = max(name_bid_amount.values())

    for name, amount in name_bid_amount.items():
        if max_amount == amount:
            return name, amount


def check_user_name(name, names):
    return name in names


def get_current_bidders():
    bidders_list = [
        {
            'John': 30
        },
        {
            'Harry': 134
        },
        {
            'Tony': 89
        },
    ]
    return bidders_list


def print_current_bidders(name_bid_amount):
    print("\nCurrent bidders:\n")
    for name, amount in sorted(name_bid_amount.items(),
                               key=lambda x: x[1],
                               reverse=True):
        print(f"{name:5}: ${amount:,}")
    print()


def get_default_bidders():
    temp = {}
    for b in get_current_bidders():
        temp.update(b)
    return temp


def user_interface():
    name_bid_amount = get_default_bidders()

    while True:
        print_current_bidders(name_bid_amount)
        user_name = get_user_name(name_bid_amount.keys())
        user_bid = get_user_bid_amount()

        name_bid_amount[user_name] = user_bid
        answer = ask_user_more_biders()

        if answer == 'n':
            break

        clear_console()

    winner, winner_bid = get_winner(name_bid_amount)
    print(f"The winner is {winner} with a bid of ${winner_bid:,}")


def main():
    print(LOGO)
    print(get_welcome_message())

    try:
        user_interface()

    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()