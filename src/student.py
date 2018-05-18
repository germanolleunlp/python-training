class Student:

    def __init__(self, name):
        self.name = name
        self.assignments = set()

    def __str__(self):
        return self.name

    def add_assignment(self, assignment):
        self.assignments.add(assignment)

    def assignments_of_teacher(self, teacher):
        return [assignment for assignment in self.assignments if assignment.teacher == teacher]
