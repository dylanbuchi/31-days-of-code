class Question:
    def __init__(self, question: str, correct_answer: str,
                 incorrect_answers: list):
        self._question = question
        self._correct_answer = correct_answer
        self._incorrect_answers = incorrect_answers

    def __repr__(self):
        return f"\nQuestion: {str(self._question)}\nAnswer: {str(self._correct_answer)}\nIncorrect Answers{self._incorrect_answers}"

    @property
    def question(self):
        return str(self._question)

    @property
    def correct_answer(self):
        return str(self._correct_answer)

    @property
    def incorrect_answers(self):
        return self._incorrect_answers
