import re

from colorama import Fore, init


class Auction:
    def __init__(self) -> None:
        init(autoreset=True)
        self.name_with_bid_amount_map = {}

    def check_user_name(self, name):
        return name in self.name_with_bid_amount_map

    def get_welcome_message(self, message="Welcome to my auction program"):
        return message

    def print_error_message(self, message):
        print(Fore.RED + message)

    def get_user_name(self):
        try:
            name = input("What's your name?\n").title().strip()
            if self.check_user_name(name):
                self.print_error_message(
                    "This name is already in our database. Please choose an username"
                )
                return self.get_user_name()

            assert re.match(r"^[a-z A-Z]+$", name) is not None

        except AssertionError:
            self.print_error_message("Please enter a valid name")
            return self.get_user_name()

        else:
            return name

    def get_user_bid_amount(self):
        try:
            bid = int(input("What's your bid?\n$").strip())
            assert bid > 0

        except (ValueError, AssertionError):
            # recursive calls until user enters a valid input
            self.print_error_message('Please enter a valid amount')
            return self.get_user_bid_amount()

        else:
            return bid

    def ask_user_more_biders(self):
        try:
            answer = input(
                "Are there any other bidders? (y/n)\n").lower().strip()[:1]
            assert answer == 'y' or answer == 'n'

        except AssertionError:
            self.print_error_message("Please enter 'yes' or 'no' (y/n)")
            return self.ask_user_more_biders()
        else:
            return answer

    def get_winner(self, name_bid_amount):
        max_amount = max(name_bid_amount.values())

        for name, amount in name_bid_amount.items():
            if max_amount == amount:
                return name, amount

    def print_current_bidders(self):
        print("\nCurrent bidders:\n")

        if self.name_with_bid_amount_map:
            for name, amount in sorted(self.name_with_bid_amount_map.items(),
                                       key=lambda x: x[1],
                                       reverse=True):
                print(f"{name:5}: ${amount:,}")
        print()
