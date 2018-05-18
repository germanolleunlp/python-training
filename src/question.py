class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        self.options = set()

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.options)

    def add_option(self, option):
        self.options.add(option)
