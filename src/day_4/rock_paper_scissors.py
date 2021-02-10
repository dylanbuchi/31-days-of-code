import random
import time
import sys


def get_game_images():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    return (rock, paper, scissors)


def get_index_from(user_choice):
    indexes = {'r': 0, 'p': 1, 's': 2}
    return indexes.get(user_choice.lower().strip()[:1], 0)


def play_again(points):
    main(points) if (choice :=
                     input("Press enter to play again or else to exit")
                     == '') else sys.exit()


def print_game_images(player, computer):
    print(f"You chose:")
    print(get_game_images()[player])
    time.sleep(1)

    print("Computer chose:")
    print(get_game_images()[computer])
    time.sleep(1)


def get_game_result(player, computer, points):

    win_combs = {
        0: 2,
        1: 0,
        2: 1,
    }

    print_game_images(player, computer)

    if (win_combs[player] == computer):

        points['You'] += 1

        return 'You win!'

    elif (win_combs[computer] == player):
        points['Computer'] += 1

        return 'You lose'

    else:
        return 'It\'s a Draw!'


def print_points(points):
    print("TOTAL POINTS:", '\n')

    for player, score in points.items():
        print(f"{player}: {score}\n")


def main(points):

    rules = ('Rock', 'Paper', 'Scissors')

    computer_choice = rules.index(random.choice(rules))

    try:
        player_choice = int(
            input("Choose Rock (1), Paper (2), or Scissors (3):\n").lower().
            strip()[:1]) - 1

    except (ValueError, IndexError):
        player_choice = random.randint(0, 2)

    result = get_game_result(player_choice, computer_choice, points)

    print(result, '\n')
    print_points(points)
    play_again(points)


if __name__ == "__main__":
    points = {'You': 0, 'Computer': 0}

    try:
        main(points)

    except KeyboardInterrupt:
        print('Exit Program')
        sys.exit()
