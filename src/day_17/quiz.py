import random
from colorama import Fore, init


class Quiz:
    def __init__(self, question_objects: list):
        self.question_objects = question_objects
        self.track_questions = []
        self.question_counter = 0
        self.player_score = 0
        self.random_string_colors = [
            Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.WHITE, Fore.YELLOW
        ]
        self.numbers_answers = {}
        self.player_lives = 3

        init(autoreset=True)

    def display_list_of_possible_answers(self, incorrect_answers,
                                         correct_answer):
        possible_answers = incorrect_answers.copy()
        possible_answers.append(correct_answer)

        random.shuffle(possible_answers)

        for index, answer in enumerate(possible_answers):
            index += 1
            print(f"\n{Fore.WHITE}{str(index)} - {Fore.YELLOW}{answer}")
            self.numbers_answers[index] = answer
        print()

    def __repr__(self):
        return """                                      
                        88            
                        ""            
                                      
 ,adPPYb,d8 88       88 88 888888888  
a8"    `Y88 88       88 88      a8P"  
8b       88 88       88 88   ,d8P'    
"8a    ,d88 "8a,   ,a88 88 ,d8"       
 `"YbbdP'88  `"YbbdP'Y8 88 888888888  
         88                           
         88        """

    def get_random_question(self):
        question = None
        while question is None or question in self.track_questions:
            if (self.check_user_has_done_every_question()):
                break
            question = random.choice(self.question_objects)

        self.track_questions.append(question)
        return question

    def check_user_has_done_every_question(self):
        return len(self.track_questions) == len(self.question_objects)

    def get_random_color_for_string(self):
        return random.choice(self.random_string_colors)

    def get_user_a_question(self):
        self.question_counter += 1
        color = self.get_random_color_for_string()
        question_object = self.get_random_question()
        question = question_object.question
        print(f"\n{color}Question {self.question_counter}:")
        print(f"\n{question}\n")
        return question_object

    def get_number_key_from_correct_answer(self, correct_answer):
        for number, answer in self.numbers_answers.items():
            if answer == correct_answer:
                return number

    def get_result_from_user_answer(self, user_answer, correct_answer):
        answer_number = self.get_number_key_from_correct_answer(correct_answer)
        return True if answer_number == user_answer else False

    def ask_user_an_answer(self, message):
        try:
            answer = int(input(message).strip())

            assert answer in self.numbers_answers
        except (AssertionError, ValueError):
            print(Fore.RED + "Please choose a correct number")
            return self.ask_user_an_answer(message)
        else:
            return answer

    def print_player_score(self):
        print(f"Score: {self.player_score}/{self.question_counter}")