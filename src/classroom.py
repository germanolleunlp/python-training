class Classroom:

  def __init__(self, teacher, students = []):
    self.teacher = teacher
    self.students = students

  def __str__(self):
    return "{}'s classroom".format(self.teacher)
