import sys
import os

sys.path.append(os.getcwd())

from calculator import Calculator
from logo import LOGO


def print_operations():
    print("""
+
-
*
/
""")


def get_user_operation(operations):
    print_operations()
    try:
        operator = input("Pick an operation: ").lower().strip()
        assert operator in operations.keys()
    except AssertionError:
        print("Select a valid operation")
        return get_user_operation(operations)
    else:
        return operator


def get_user_number(string):
    try:
        number = float(input(f"\nPick the {string} number: "))

    except ValueError:
        print("Error, only numbers allowed")
        return get_user_number(string)

    else:
        return int(number) if (str(number)[-1] == '0') else number


def get_user_inputs(operations):

    number_1 = get_user_number('first')
    operation = get_user_operation(operations)
    number_2 = get_user_number('second')

    return number_1, number_2, operation


def print_result(n1, n2, operator, result):
    print(f"{n1} {operator} {n2} = {result}")


def calculate_user_numbers(n1, n2, operator, operations):
    calculate = operations[operator]
    result = calculate(n1, n2)
    return result


def user_interface():
    calculator = Calculator()
    operations = calculator.get_operations()
    number_1, number_2, operator = get_user_inputs(operations)

    result = calculate_user_numbers(number_1, number_2, operator, operations)
    print_result(number_1, number_2, operator, result)
    current_num = result

    choice = ''

    while choice == '':

        choice = input(
            f"Press enter to keep calculating with the number {current_num}\n")
        if not choice:
            operation = get_user_operation(operations)
            next_num = get_user_number('next')
            result = calculate_user_numbers(current_num, next_num, operation,
                                            operations)
            print_result(current_num, next_num, operation, result)
            current_num = result

    run_again("\nPress enter to use the calculator again\n", main)


def run_again(string, func):
    choice = input(string).lower().strip()
    if not choice:
        func()


def main():
    print(LOGO)
    try:
        user_interface()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()