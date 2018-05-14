class Classroom:

    def __init__(self, teacher):
        self.teacher = teacher
        self.students = set()

    def __str__(self):
        return "{}'s classroom with {} students".format(self.teacher, len(self))

    def __len__(self):
        return len(self.students)

    def add_student(self, student):
        self.students.add(student)
