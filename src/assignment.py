from src.answer import Answer


class Assignment:

    def __init__(self, teacher, student, quiz):
        self.teacher = teacher
        self.student = student
        self.quiz = quiz
        self.total_of_questions = len(quiz.questions)
        self.wrong_answers = set()
        self.correct_answers = set()
        self.grade = 0

    def __str__(self):
        return '{}: {} for {} assigned by {}'.format(self.student, self.grade, self.quiz, self.teacher)

    def add_answer(self, question, option):
        answer = Answer(self.student, question, option)

        if answer.correct():
            self.correct_answers.add(answer)
        else:
            self.wrong_answers.add(answer)

        self.set_grade(self._calculate_grade())

    def set_grade(self, grade):
        self.grade = grade

    def _calculate_grade(self):
        return round(len(self.correct_answers) / self.total_of_questions, 1) * 10
