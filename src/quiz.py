class Quiz:

    def __init__(self, teacher, questions):
        self.teacher = teacher
        self.questions = questions
        self.answers = set()

    def __str__(self):
        return "{}'s quiz".format(self.teacher)

    def __len__(self):
        return len(self.questions)

    def add_question(self, question):
        self.questions.add(question)

    def add_answer(self, answer):
        self.answers.add(answer)

    def answers_of(self, student):
        return {answer for answer in self.answers if answer.student == student}
