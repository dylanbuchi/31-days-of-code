# Fizz Buzz
import sys
import pyttsx3

from colorama import init, Fore
from logo import LOGO


def play_fizz_buzz(limit):
    fizzBuzz = 'FizzBuzz'
    fizz = 'Fizz'
    buzz = 'Buzz'

    engine = pyttsx3.init()

    for i in range(1, limit + 1):
        end_line = ', ' if i < limit else '.\n'
        if i % 15 == 0:
            print(Fore.CYAN + fizzBuzz, end=end_line)
            engine.say(fizzBuzz)
        elif i % 5 == 0:
            print(Fore.YELLOW + buzz, end=end_line)
            engine.say(buzz)
        elif i % 3 == 0:
            print(Fore.GREEN + fizz, end=end_line)
            engine.say(fizz)
        else:
            print(i, end=end_line)
            engine.say(i)
        engine.runAndWait()


def main():
    init(autoreset=True)
    print(Fore.RED + LOGO)
    try:
        play_fizz_buzz(15)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
