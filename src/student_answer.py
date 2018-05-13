class StudentAnswer:

  def __init__(self, student, answer, question, quiz):
    self.student = student
    self.answer = answer
    self.question = question
    self.quiz = quiz

  def __str__(self):
    return '{} answer {} for question {} in quiz {}'.format(
      self.student,
      self.answer,
      self.question,
      self.quiz
    )
