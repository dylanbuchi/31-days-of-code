# Quiz
import os
import sys
import requests

from colorama import Fore, init

from question import Question
from quiz import Quiz


def get_questions_data_from(url):
    response = requests.get(url)
    return response.json()['results']


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_questions_from(questions_dict):
    question_objects = []

    for q in questions_dict:
        question = remove_unreadable_parts(q['question'])
        correct_answer = remove_unreadable_parts(q['correct_answer'])
        incorrect_answers = remove_unreadable_parts(q['incorrect_answers'])

        question_objects.append(
            Question(question, correct_answer, incorrect_answers))
    return question_objects


def run_quiz(quiz: Quiz):
    clear_console()
    print(quiz)

    while True:
        question_object = quiz.get_user_a_question()
        correct_answer = question_object.correct_answer
        # question = question_object.question
        incorrect_answers = question_object.incorrect_answers
        quiz.display_list_of_possible_answers(incorrect_answers,
                                              correct_answer)
        user_answer = quiz.ask_user_an_answer("Answer: ")
        result = quiz.get_result_from_user_answer(user_answer, correct_answer)

        string_false_answer = f"{Fore.RED}False!\n{Fore.WHITE}The correct answer is:{Fore.GREEN} {correct_answer}\n"
        string_correct_answer = f"{Fore.GREEN}Correct!\n"

        if result:
            clear_console()
            print("*" * 55)
            print(string_correct_answer)
            quiz.player_score += 1

        else:
            clear_console()
            print(string_false_answer)
            quiz.player_lives -= 1
            print("*" * 55)

        if quiz.check_user_has_done_every_question():
            clear_console()
            print(
                f"{Fore.BLUE} Congratulations! You finished the whole Quiz without losing!!"
            )
            quiz.print_player_score()
            break

        if not quiz.player_lives:
            quiz.print_player_score()
            print(
                f"{Fore.RED}No more lives left...{Fore.RESET} Do you want to try again? (y/n)"
            )
            play_again()
        quiz.print_player_score()


def play_again():
    choice = input().strip().lower()
    return main() if choice == 'y' else sys.exit()


def remove_unreadable_parts(string):
    if '&' in string and ';' in string:
        start = string.index('&')
        end = string.index(';')
        word = string[start:end + 1]
        result = string.replace(word, '')
        return result
    else:
        return string


def remove_unreadable_parts_from_list(question_objects):
    for q in question_objects:
        for string in q.incorrect_answers:
            index = q.incorrect_answers.index(string)
            q.incorrect_answers[index] = remove_unreadable_parts(string)


def main():
    init(autoreset=True)
    # file_path = os.path.join(os.getcwd(), 'src', 'day_17', 'data.txt')
    quiz_data = get_questions_data_from(
        "https://opentdb.com/api.php?amount=48&category=18")

    question_objects = get_questions_from(quiz_data)
    remove_unreadable_parts_from_list(question_objects)

    quiz = Quiz(question_objects)
    run_quiz(quiz)


if __name__ == "__main__":
    main()