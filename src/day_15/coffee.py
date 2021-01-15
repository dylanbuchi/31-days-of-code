import sys
import time
from colorama import init, Fore


class CoffeeIngredients:
    def __init__(self, water: int, milk: int, coffee_beans: int):
        self._water = water
        self._milk = milk
        self._coffee_beans = coffee_beans

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, new_value):
        if (new_value <= 0):
            self._water = 0
        else:
            self._water = new_value

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, new_value):
        if (new_value <= 0):
            self._milk = 0
        else:
            self._milk = new_value

    @property
    def coffee_beans(self):
        return self._coffee_beans

    @coffee_beans.setter
    def coffee_beans(self, new_value):
        if (new_value <= 0):
            self._coffee_beans = 0
        else:
            self._coffee_beans = new_value

    def __repr__(self):
        return f"""{Fore.BLUE}Water: {self.water:>12}ml
{Fore.WHITE}Milk: {self.milk:>13}ml
{Fore.LIGHTYELLOW_EX}Coffee beans: {self.coffee_beans:>5}g
"""


class Coffee:
    def __init__(self, ingredients: CoffeeIngredients, price: float):
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return f"{self.ingredients}{Fore.GREEN}Money:  {'$'+ str(self.price):>9}"

    def get_water(self):
        return self.ingredients.water

    def get_milk(self):
        return self.ingredients.milk

    def get_coffee_beans(self):
        return self.ingredients.coffee_beans


class Latte(Coffee):
    def __init__(self, water, milk, coffee_beans, price):
        super().__init__(CoffeeIngredients(water, milk, coffee_beans), price)
        self.name = 'Latte'

    def __repr__(self):
        return f"Latte:\n\n{Coffee.__repr__(self)}"


class Cappuccino(Coffee):
    def __init__(self, water, milk, coffee_beans, price):
        super().__init__(CoffeeIngredients(water, milk, coffee_beans), price)
        self.name = 'Cappuccino'

    def __repr__(self):
        return f"Cappuccino:\n\n{Coffee.__repr__(self)}"


class Espresso(Coffee):
    def __init__(self, water, milk, coffee_beans, price):
        super().__init__(CoffeeIngredients(water, milk, coffee_beans), price)
        self.name = 'Espresso'

    def __repr__(self):
        return f"Espresso:\n\n{Coffee.__repr__(self)}"


class CoffeeMachine:
    def __init__(self, ingredients: CoffeeIngredients, coffees: list,
                 total_money: float):
        self.ingredients = ingredients
        self._total_money = total_money
        self.coffees = coffees

    def get_logo(self):
        return """      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
"""

    def shut_down_coffee_machine(self):
        print("The coffee machine is shutting down..")
        sys.exit()

    def ask_user_to_pay_coffee(self, coffee_name, price):
        try:
            user_money = float(
                input(
                    f"{coffee_name} costs ${price:.2f}, please insert the money here: $"
                ))
            assert user_money >= price

            if (user_money > self.total_money):
                print(
                    Fore.RED +
                    f"Sorry! I only have ${self.total_money}, please enter a correct amount"
                )
                return self.ask_user_to_pay_coffee(coffee_name, price)
        except (ValueError, AssertionError):
            print(Fore.RED + "Error, please enter a correct amount")
            return self.ask_user_to_pay_coffee(coffee_name, price)

        else:
            return user_money

    def prepare_coffee(self, coffee_name: str):
        for coffee in self.coffees:
            if coffee.name == coffee_name:
                can_make_coffee = self.check_enough_ingredients_to_make_a_coffee(
                    coffee)

                if can_make_coffee:
                    user_money = self.ask_user_to_pay_coffee(
                        coffee.name, coffee.price)

                    user_has_money = self.check_user_has_enough_money(
                        user_money,
                        coffee.price,
                    )
                    machine_has_money = self.check_machine_has_enough_money(
                        user_money)

                    if (user_has_money and machine_has_money):
                        self.make_coffee(coffee, coffee_name)
                        return self.give_user_change(user_money, coffee)

                else:
                    return False

    def pause_coffee_machine(self, seconds):
        print('...')
        time.sleep(seconds)

    def check_machine_has_enough_money(self, user_money):
        return self.total_money >= user_money

    def check_user_has_enough_money(self, user_money: float,
                                    coffee_price: float):
        return user_money >= coffee_price

    def give_user_change(self, user_money: float, coffee: Coffee):
        coffee_price = coffee.price
        change = user_money - coffee_price
        self.total_money += coffee_price
        return change

    def make_coffee(self, coffee: Coffee, coffee_name: str):
        print(f"Preparing your {coffee_name}!")
        self.pause_coffee_machine(1.5)
        print(f"\nHere is your {coffee.name} ☕. Enjoy!")

        coffee_water = coffee.get_water()
        coffee_milk = coffee.get_milk()
        coffee_beans = coffee.get_coffee_beans()

        self.ingredients.water = self.ingredients.water - coffee_water
        self.ingredients.milk = self.ingredients.milk - coffee_milk
        self.ingredients.coffee_beans = self.ingredients._coffee_beans - coffee_beans

    def check_enough_ingredients_to_make_a_coffee(self, coffee: Coffee):
        total_water = self.ingredients.water
        total_milk = self.ingredients.milk
        total_coffee_beans = self.ingredients.coffee_beans

        if (total_water < coffee.get_water() or total_water <= 0):
            print(Fore.RED + f"Not enough water to make a {coffee.name}")
            return False
        elif (total_milk < coffee.get_milk() or total_milk <= 0):
            print(Fore.RED + f"Not enough milk to make a {coffee.name}")
            return False
        elif total_coffee_beans < coffee.get_coffee_beans(
        ) or total_coffee_beans <= 0:
            print(Fore.RED +
                  f"Not enough coffee beans to make a {coffee.name}")
            return False
        else:
            return True

    def print_report(self):
        print("Coffee Machine: \n")
        print(
            f"{self.ingredients}{Fore.GREEN}Money: {'$'+ str(self.total_money):>12}"
        )

    @property
    def total_money(self):
        return self._total_money

    @total_money.setter
    def total_money(self, new_value):
        self._total_money = new_value
