class Classroom:

  def __init__(self, teacher, students = ()):
    self.teacher = teacher
    self.students = students

  def __str__(self):
    return "{}'s classroom with {} students".format(self.teacher, len(self))

  def __len__(self):
    return len(self.students)
