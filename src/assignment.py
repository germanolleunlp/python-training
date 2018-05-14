class Assignment:

    def __init__(self, quiz, student):
        self.quiz = quiz
        self.student = student
        self.grade = 0

    def __str__(self):
        return '{}: {}'.format(self.student, self.grade)

    def add_answer(self, answer):
        self.quiz.add_answer(answer)

    def set_grade(self, grade):
        self.grade = grade
