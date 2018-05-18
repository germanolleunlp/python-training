class Quiz:

    def __init__(self):
        self.questions = set()

    def __str__(self):
        return "Quiz with {} questions".format(len(self))

    def __len__(self):
        return len(self.questions)

    def add_question(self, question):
        self.questions.add(question)
