class Assignment:

    def __init__(self, quiz, student):
        self.quiz = quiz
        self.student = student
        self.grade = 0

    def __str__(self):
        return '{}: {}'.format(self.student, self.grade)

    def add_answer(self, answer):
        self.quiz.add_answer(answer)
        self.set_grade(self._calculate_grade())

    def set_grade(self, grade):
        self.grade = grade

    def _calculate_grade(self):
        correct_answers = self.quiz.correct_answers_of_student(self.student)
        return round(len(correct_answers) / len(self.quiz), 1) * 10
