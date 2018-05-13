class Quiz:

  def __init__(self, teacher, questions = ()):
    self.teacher = teacher
    self.questions = questions

  def __str__(self):
    return "{}'s quiz".format(self.teacher)

  def __len__(self):
    return len(self.questions)
