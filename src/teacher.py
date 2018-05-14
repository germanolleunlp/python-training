from src.assignment import Assignment
from src.helpers.grades import calculate_average_grades


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
            raise BaseException("This teacher can not correct for {}".format(classroom))

        assignments = [assignment for assignment in self.assignments if assignment.student in classroom.students]
        return calculate_average_grades(assignments)

    def calculate_global_average(self):
        return calculate_average_grades(assignments=self.assignments)
