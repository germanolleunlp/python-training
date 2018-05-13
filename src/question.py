class Question:

  def __init__(self, text, answer, options = ()):
    self.text = text
    self.answer = answer
    self.options = options

  def __str__(self):
    return self.text

  def __len__(self):
    return len(self.options)
