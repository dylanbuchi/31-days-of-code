import sys
import os
import time
from colorama import init, Fore

from coffee import CoffeeIngredients, CoffeeMachine, Latte, Cappuccino, Espresso


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_user_coffee_machine_commands(string, error_msg):
    commands = ['1', '2', '3', 'off', 'report']

    try:
        choice = input(string).strip().lower()
        assert choice in commands
    except (AssertionError, ValueError):
        clear_console()
        print(Fore.RED + error_msg)
        return ask_user_coffee_machine_commands(string, error_msg)
    else:
        return choice


def get_default_coffees():
    coffees = [
        Latte(water=200, milk=150, coffee_beans=24, price=2.5),
        Cappuccino(water=250, milk=100, coffee_beans=24, price=3.0),
        Espresso(water=50, milk=0, coffee_beans=18, price=1.5),
    ]
    return coffees


def get_default_coffee_ingredients():
    return CoffeeIngredients(water=500, milk=500, coffee_beans=500)


def print_coffee_machine_report(coffee_machine):
    coffee_machine.print_report()


def get_coffee(coffee_machine, coffee_name):
    for coffee in coffee_machine.coffees:
        if coffee.name == coffee_name:
            coffee_machine.check_enough_ingredients_to_make_a_coffee(coffee)


def make_user_coffee(coffee_machine: CoffeeMachine, user_choice):
    choices_coffees = {'1': 'Latte', '2': 'Espresso', '3': 'Cappuccino'}
    change = coffee_machine.prepare_coffee(choices_coffees[user_choice])

    time.sleep(1.2)
    if change:
        print(f"\nHere is your change: ${change:.2f}!\n")

    elif change == False:
        coffee_name = choices_coffees[user_choice]
        if not coffee_machine.ingredients.water:
            print(Fore.RED + f"No more water to make a coffee!")
        elif not coffee_machine.ingredients.milk:
            print(Fore.RED + f"No more milk to make a coffee!")
        elif not coffee_machine.ingredients._coffee_beans:
            print(Fore.RED + f"No more coffee beans to make a coffee!")

        coffee_machine.print_report()
        print("\nSomeone will come to refill the machine, come back later!")
        coffee_machine.shut_down_coffee_machine()
    else:
        return False


def ask_user_another_coffee(coffee_machine):
    try:

        choice = input(
            "Do you want to buy another coffee ? (y/n)").strip().lower()[:1]
        assert choice in 'yn'
    except AssertionError:
        print(Fore.RED + "PLease enter 'y' for yes or 'n' for no\n")
        return ask_user_another_coffee(coffee_machine)
    else:
        return choice


def user_interface(coffee_machine):

    clear_console()

    print(Fore.YELLOW + coffee_machine.get_logo())

    while True:
        special_commands = {
            'off': coffee_machine.shut_down_coffee_machine,
            'report': coffee_machine.print_report
        }

        choice = ask_user_coffee_machine_commands(
            "Choose a coffee to buy: (1) Latte - (2) Espresso - (3) Cappuccino: ",
            "Please enter a valid command")
        clear_console()

        if choice not in special_commands:
            make_user_coffee(coffee_machine, choice)
            another_coffee = ask_user_another_coffee(coffee_machine)
            if another_coffee == 'y':
                clear_console()
                user_interface(coffee_machine)
            else:
                print('Ok bye')
                sys.exit()
        else:
            special_function = special_commands[choice]
            special_function()


def main():
    coffee_machine = CoffeeMachine(
        ingredients=get_default_coffee_ingredients(),
        total_money=12,
        coffees=get_default_coffees())

    init(autoreset=True)
    try:
        user_interface(coffee_machine)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()