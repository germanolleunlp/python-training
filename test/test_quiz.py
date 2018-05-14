from unittest import TestCase

from src.teacher import Teacher
from src.student import Student
from src.question import Question
from src.quiz import Quiz
from src.answer import Answer
from src.classroom import Classroom

jude = Student(name='Jude Arroyo')
carlee = Student(name='Carlee Holloway')
julia = Student(name='Julia Henderson')
earl = Student(name='Earl Christensen')

question_one = Question(
    text='What is the national sport in Japan?',
    answer='Judo',
    options=('Judo', 'Baseball', 'Sumo Wrestling')
)

question_two = Question(
    text='How many minutes is a rugby match?',
    answer=80,
    options=(70, 80, 90)
)

question_three = Question(
    text='Which car won Fernando Alonso his first tittle in Formula 1 with?',
    answer='Renault',
    options=('Renault', 'Ford', 'Peugeot')
)

question_four = Question(
    text='In which sport can you win the Davis Cup?',
    answer='Tennis',
    options=('Football', 'Racing', 'Tennis')
)

question_five = Question(
    text="In which year did Maradona score a goal with his hand?",
    answer=1986,
    options=(1983, 1986, 1988)
)

questions = {question_one, question_two, question_three, question_four, question_five}


class TestQuiz(TestCase):

    def setUp(self):
        self.teacher = Teacher(name='Leon Lang')

    def tearDown(self):
        self.teacher.assignments.clear()

    def test_len(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        self.assertEqual(len(quiz), 5)

    def test_grade_for_full_quiz_completed(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        assignment = self.teacher.assign(quiz, julia)
        assignment.add_answer(Answer(student=julia, question=question_one, option='Judo'))
        assignment.add_answer(Answer(student=julia, question=question_two, option=80))
        assignment.add_answer(Answer(student=julia, question=question_three, option='Renault'))
        assignment.add_answer(Answer(student=julia, question=question_four, option='Tennis'))
        assignment.add_answer(Answer(student=julia, question=question_five, option=1986))

        self.assertEqual(assignment.grade, 10)

    def test_grade_for_partial_quiz_completed(self):
        quiz = Quiz(teacher=self.teacher, questions=questions)
        assignment = self.teacher.assign(quiz, carlee)
        assignment.add_answer(Answer(student=carlee, question=question_one, option='Judo'))
        assignment.add_answer(Answer(student=carlee, question=question_two, option=80))
        assignment.add_answer(Answer(student=carlee, question=question_three, option='Renault'))

        self.assertEqual(assignment.grade, 6)

    def test_calculate_global_average(self):
        quiz_one = Quiz(teacher=self.teacher, questions=questions)
        quiz_two = Quiz(teacher=self.teacher, questions=questions)

        for student in [jude, julia, carlee, earl]:
            assignment = self.teacher.assign(quiz_one, student)
            assignment.add_answer(Answer(student=student, question=question_one, option='Judo'))
            assignment.add_answer(Answer(student=student, question=question_two, option=80))
            assignment.add_answer(Answer(student=student, question=question_three, option='Renault'))
            assignment.add_answer(Answer(student=student, question=question_four, option='Tennis'))
            assignment.add_answer(Answer(student=student, question=question_five, option=1986))
            assignment = self.teacher.assign(quiz_two, student)
            assignment.add_answer(Answer(student=student, question=question_one, option='Judo'))
            assignment.add_answer(Answer(student=student, question=question_two, option=80))
            assignment.add_answer(Answer(student=student, question=question_three, option='Renault'))

        self.assertEqual(self.teacher.calculate_global_average(), {
            'Carlee Holloway': 8.0,
            'Earl Christensen': 8.0,
            'Jude Arroyo': 8.0,
            'Julia Henderson': 8.0,
        })

    def test_calculate_average_of_classroom(self):
        classroom = Classroom(teacher=self.teacher, students={jude, carlee})
        quiz_one = Quiz(teacher=self.teacher, questions=questions)
        quiz_two = Quiz(teacher=self.teacher, questions=questions)

        for student in [jude, julia, carlee, earl]:
            assignment = self.teacher.assign(quiz_one, student)
            assignment.add_answer(Answer(student=student, question=question_one, option='Judo'))
            assignment.add_answer(Answer(student=student, question=question_two, option=80))
            assignment.add_answer(Answer(student=student, question=question_three, option='Renault'))
            assignment.add_answer(Answer(student=student, question=question_four, option='Tennis'))
            assignment.add_answer(Answer(student=student, question=question_five, option=1986))
            assignment = self.teacher.assign(quiz_two, student)
            assignment.add_answer(Answer(student=student, question=question_one, option='Judo'))
            assignment.add_answer(Answer(student=student, question=question_two, option=80))
            assignment.add_answer(Answer(student=student, question=question_three, option='Renault'))

        self.assertEqual(self.teacher.calculate_average_of_classroom(classroom), {
            'Carlee Holloway': 8.0,
            'Jude Arroyo': 8.0,
        })

    def test_calculate_average_of_classroom_with_invalid_teacher(self):
        classroom = Classroom(teacher=Teacher(name='Selena Francis'))
        classroom.add_student(julia)
        error_message = 'This teacher can not correct for classroom of Selena Francis with 1 students'
        with self.assertRaises(BaseException) as context:
            self.teacher.calculate_average_of_classroom(classroom)

        self.assertTrue(error_message in str(context.exception))
