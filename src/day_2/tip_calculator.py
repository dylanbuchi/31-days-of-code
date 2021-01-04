import sys

# Tip Calculator


def run_tip_calculator():
    print("Welcome to the tip calculator.")

    total_bill = float(input("What was the total bill?\n$"))
    check_bill(total_bill)

    percentage_tip = check_percentage(
        int(input("Choose a percentage tip you would like to give:\n")))

    total_people = check_people(
        int(input("How many people to split the bill?\n")))

    total_to_pay = calculate_tip(total_bill, percentage_tip, total_people)

    print(f"You have to pay ", end='') if total_people == 1 else print(
        f"Each person should pay ", end='')

    print(f"${total_to_pay:.2f}")


def calculate_tip(total_bill, percentage_tip, total_people):
    percentage = percentage_tip / 100 * total_bill
    total = (total_bill + percentage) / total_people
    return total


def check_bill(total):
    if total <= 0:
        print("It's on the house!")
        sys.exit()


def check_people(total):
    return 1 if total <= 0 else total


def check_percentage(total):
    return 0 if total <= 0 else total


def main():
    run_tip_calculator()


if __name__ == "__main__":
    main()