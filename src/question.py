class Question:

  def __init__(self, answer, options):
    self.answer = answer
    self.options = options

  def __str__(self):
    return ', '.join(self.options)
