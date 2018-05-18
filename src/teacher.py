from src.assignment import Assignment
from src.helpers.grades import calculate_average_grades


class Teacher:

    def __init__(self, name):
        self.name = name
        self.assignments = set()

    def __str__(self):
        return self.name

    def assign(self, quiz, student):
        assignment = Assignment(self, student, quiz)
        student.add_assignment(assignment)
        self.assignments.add(assignment)
        return assignment

    def calculate_average_of_classroom(self, classroom):
        if classroom.teacher != self:
            raise BaseException("This teacher can not correct for {}".format(classroom))

        return (self._average_grade_for_student(student) for student in classroom.students)

    def calculate_global_average(self):
        return calculate_average_grades(self.assignments)

    def _average_grade_for_student(self, student):
        return calculate_average_grades(student.assignments_of_teacher(self))
