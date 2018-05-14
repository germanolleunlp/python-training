class Answer:

    def __init__(self, student, question, option):
        self.student = student
        self.question = question
        self.option = option

    def __str__(self):
        return '{} answer {} for question {}'.format(self.student, self.option, self.question)

    def correct(self):
        return self.option == self.question.answer
