from statistics import mean
from src.assignment import Assignment


def calculate_average_grades(assignments):
    grades = {}

    for assignment in assignments:
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

    def calculate_average_of_classroom(self, classroom):
        if classroom.teacher != self:
            raise BaseException('This teacher can not correct this classroom')

        assignments = [assignment for assignment in self.assignments if assignment.student in classroom.students]
        return calculate_average_grades(assignments)

    def calculate_global_average(self):
        return calculate_average_grades(assignments=self.assignments)

    def correct_assignment(self, assignment):
        quiz = assignment.quiz

        if quiz.teacher != self:
            raise BaseException('This teacher can not correct the quiz')

        correct_answers = quiz.correct_answers_of_student(assignment.student)
        grade = round(len(correct_answers) / len(quiz), 1) * 10
        assignment.set_grade(grade)
        return assignment
