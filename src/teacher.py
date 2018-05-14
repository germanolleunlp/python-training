from statistics import mean

from src.assignment import Assignment


class Teacher:

    def __init__(self, name):
        self.name = name
        self.assignments = set()

    def __str__(self):
        return self.name

    def assign(self, quiz, student):
        assignment = Assignment(quiz=quiz, student=student)
        self.assignments.add(assignment)

        return assignment

    def calculate_grades(self):
        grades = {}

        for assignment in self.assignments:
            student = assignment.student.name
            try:
                grades[student]
            except KeyError:
                grades[student] = []
            finally:
                grades[student].append(assignment.grade)

        for student in grades:
            grades[student] = mean(grades[student])

        return grades

    def correct_assignment(self, assignment):
        quiz = assignment.quiz

        if quiz.teacher == self:
            student = assignment.student
            correct_answers = {answer for answer in quiz.answers_of(student) if answer.correct()}
            grade = round(len(correct_answers) / len(quiz), 1) * 10
            assignment.set_grade(grade)
            return assignment
        else:
            raise BaseException('This teacher can not correct the quiz')
