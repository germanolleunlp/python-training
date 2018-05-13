class StudentAnswer:
  
  def __init__(self, student, question, answer):
    self.student = student
    self.question = question
    self.answer = answer
  
  def __str__(self):
    return '{} answer {} for question {}'.format(
      self.student,
      self.answer,
      self.question
    )
