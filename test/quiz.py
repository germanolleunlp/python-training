import unittest

from src.teacher import Teacher
from src.student import Student
from src.question import Question
from src.quiz import Quiz
from src.answer import Answer

jude = Student(name='Jude Arroyo')
carlee = Student(name='Carlee Holloway')
julia = Student(name='Julia Henderson')
earl = Student(name='Earl Christensen')

question_one = Question(
    text='What is the national sport in Japan?',
    answer=1,
    options=('Judo', 'Baseball', 'Sumo Wrestling')
)

question_two = Question(
    text='How many minutes is a rugby match?',
    answer=2,
    options=(70, 80, 90)
)

question_three = Question(
    text='Which car won Fernando Alonso his first tittle in Formula 1 with?',
    answer=1,
    options=('Renault', 'Ford', 'Peugeot')
)

question_four = Question(
    text='In which sport can you win the Davis Cup?',
    answer=3,
    options=('Football', 'Racing', 'Tennis')
)

question_five = Question(
    text="In which year did Maradona score a goal with his hand?",
    answer=2,
    options=(1983, 1986, 1988)
)

questions = {question_one, question_two, question_three, question_four, question_five}


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher(name='Leon Lang')

    def test_len(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        self.assertEqual(len(quiz), 5)

    def test_correct_full_quiz_submitted(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        assignment = self.teacher.assign(quiz, julia)
        assignment.add_answer(Answer(student=julia, question=question_one, option=1))
        assignment.add_answer(Answer(student=julia, question=question_two, option=1))
        assignment.add_answer(Answer(student=julia, question=question_three, option=1))
        assignment.add_answer(Answer(student=julia, question=question_four, option=3))
        assignment.add_answer(Answer(student=julia, question=question_five, option=1))
        self.teacher.correct_assignment(assignment)

        self.assertEqual(assignment.grade, 6)

    def test_correct_partial_quiz_submitted(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        assignment = self.teacher.assign(quiz, carlee)
        assignment.add_answer(Answer(student=carlee, question=question_one, option=1))
        assignment.add_answer(Answer(student=carlee, question=question_two, option=2))
        assignment.add_answer(Answer(student=carlee, question=question_three, option=1))
        self.teacher.correct_assignment(assignment)

        self.assertEqual(assignment.grade, 6)

    def test_correct_quiz_with_invalid_teacher(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        selena = Teacher(name='Selena Francis')
        with self.assertRaises(BaseException) as context:
            selena.correct_assignment(selena.assign(quiz, carlee))

        self.assertTrue('This teacher can not correct the quiz' in str(context.exception))

    def test_calculate_grades(self):
        quiz_one = Quiz(teacher=self.teacher, questions=questions)
        quiz_two = Quiz(teacher=self.teacher, questions=questions)

        for student in [jude, julia, carlee, earl]:
            assignment = self.teacher.assign(quiz_one, student)
            assignment.add_answer(Answer(student=student, question=question_one, option=1))
            assignment.add_answer(Answer(student=student, question=question_two, option=1))
            assignment.add_answer(Answer(student=student, question=question_three, option=1))
            assignment.add_answer(Answer(student=student, question=question_four, option=3))
            assignment.add_answer(Answer(student=student, question=question_five, option=1))
            self.teacher.correct_assignment(assignment)

            assignment = self.teacher.assign(quiz_two, student)
            assignment.add_answer(Answer(student=student, question=question_one, option=1))
            assignment.add_answer(Answer(student=student, question=question_two, option=1))
            assignment.add_answer(Answer(student=student, question=question_three, option=1))
            self.teacher.correct_assignment(assignment)

        self.assertEqual(self.teacher.calculate_grades(), {
            'Carlee Holloway': 5.0,
            'Earl Christensen': 5.0,
            'Jude Arroyo': 5.0,
            'Julia Henderson': 5.0,
        })


if __name__ == '__main__':
    unittest.main()
