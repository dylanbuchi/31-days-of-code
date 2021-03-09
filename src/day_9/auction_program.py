# Auction_Program
import os
import sys
import random

sys.path.append(os.path.join(os.getcwd(), 'src'))

from day_9.auction import Auction
from day_9.logo import LOGO


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_bid(start=1, end=2000):
    return random.randint(start, end)


def get_random_name_and_remove_it_from(names):
    name = random.choice(names)
    names.remove(name)
    return name


def create_default_bidders():
    names = ["John", "Harry", "Joe", "Tony", "Emma", "Mia"]

    bidders_list = [{
        get_random_name_and_remove_it_from(names): get_random_bid()
        for i in range(6)
    }]

    return bidders_list


def get_default_bidders():
    temp = {}
    for b in create_default_bidders():
        temp.update(b)
    return temp


def user_interface():
    auction = Auction()
    print(auction.get_welcome_message())

    auction.name_with_bid_amount_map = get_default_bidders()
    name_bid_amount = auction.name_with_bid_amount_map

    while True:
        auction.print_current_bidders()

        user_name = auction.get_user_name()
        user_bid = auction.get_user_bid_amount()

        name_bid_amount[user_name] = user_bid
        answer = auction.ask_user_more_biders()

        if answer == 'n':
            break

        clear_console()

    winner, winner_bid = auction.get_winner(name_bid_amount)
    print(f"The winner is {winner} with a bid of ${winner_bid:,}")


def main():
    print(LOGO)

    try:
        user_interface()

    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()