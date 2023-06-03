class Question:
    def __init__(self, question_text: str, correct_option: int, options: list):
        self.question_text = question_text
        self.correct_option = correct_option
        self.options = options