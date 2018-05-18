from unittest import TestCase

from src.teacher import Teacher
from src.student import Student
from src.question import Question
from src.quiz import Quiz
from src.classroom import Classroom

jude = Student('Jude Arroyo')
carlee = Student('Carlee Holloway')
julia = Student('Julia Henderson')
earl = Student('Earl Christensen')

question_one = Question('What is the national sport in Japan?', 'Judo')
question_one.add_option('Judo')
question_one.add_option('Baseball')
question_one.add_option('Sumo Wrestling')

question_two = Question('How many minutes is a rugby match?', 80)
question_two.add_option(70)
question_two.add_option(80)
question_two.add_option(90)

question_three = Question('Which car won Fernando Alonso his first tittle in Formula 1 with?', 'Renault')
question_three.add_option('Renault')
question_three.add_option('Ford')
question_three.add_option('Peugeot')

question_four = Question('In which sport can you win the Davis Cup?', 'Tennis')
question_four.add_option('Football')
question_four.add_option('Racing')
question_four.add_option('Tennis')

question_five = Question("In which year did Maradona score a goal with his hand?", 1986)
question_five.add_option(1983)
question_five.add_option(1986)
question_five.add_option(1988)

questions = {question_one, question_two, question_three, question_four, question_five}


class TestQuiz(TestCase):

    def setUp(self):
        self.teacher = Teacher('Leon Lang')
        self.quiz = Quiz()
        self.quiz.add_question(question_one)
        self.quiz.add_question(question_two)
        self.quiz.add_question(question_three)
        self.quiz.add_question(question_four)
        self.quiz.add_question(question_five)

    def tearDown(self):
        self.teacher.assignments.clear()

    def test_len(self):
        self.assertEqual(len(self.quiz), 5)

    def test_grade_for_full_quiz_completed(self):
        assignment = self.teacher.assign(self.quiz, julia)
        assignment.add_answer(question_one, 'Judo')
        assignment.add_answer(question_two, 80)
        assignment.add_answer(question_three, 'Renault')
        assignment.add_answer(question_four, 'Tennis')
        assignment.add_answer(question_five, 1986)

        self.assertEqual(assignment.grade, 10)

    def test_grade_for_partial_quiz_completed(self):
        assignment = self.teacher.assign(self.quiz, carlee)
        assignment.add_answer(question_one, 'Judo')
        assignment.add_answer(question_two, 80)
        assignment.add_answer(question_three, 'Renault')

        self.assertEqual(assignment.grade, 6)

    def test_calculate_global_average(self):
        quiz_two = Quiz()

        for question in questions:
            quiz_two.add_question(question)

        for student in [jude, julia, carlee, earl]:
            assignment = self.teacher.assign(self.quiz, student)
            assignment.add_answer(question_one, 'Judo')
            assignment.add_answer(question_two, 80)
            assignment.add_answer(question_three, 'Renault')
            assignment.add_answer(question_four, 'Tennis')
            assignment.add_answer(question_five, 1986)

            assignment = self.teacher.assign(quiz_two, student)
            assignment.add_answer(question_one, 'Judo')
            assignment.add_answer(question_two, 80)
            assignment.add_answer(question_three, 'Renault')

        self.assertEqual(self.teacher.calculate_global_average(), {
            'Carlee Holloway': 8.0,
            'Earl Christensen': 8.0,
            'Jude Arroyo': 8.0,
            'Julia Henderson': 8.0,
        })

    def test_calculate_average_of_classroom(self):
        classroom = Classroom(self.teacher)
        classroom.add_student(jude)
        classroom.add_student(carlee)

        quiz_two = Quiz()
        for question in questions:
            quiz_two.add_question(question)

        for student in [jude, julia, carlee, earl]:
            assignment = self.teacher.assign(self.quiz, student)
            assignment.add_answer(question_one, 'Judo')
            assignment.add_answer(question_two, 80)
            assignment.add_answer(question_three, 'Renault')
            assignment.add_answer(question_four, 'Tennis')
            assignment.add_answer(question_five, 1986)

            assignment = self.teacher.assign(quiz_two, student)
            assignment.add_answer(question_one, 'Judo')
            assignment.add_answer(question_two, 80)
            assignment.add_answer(question_three, 'Renault')

        generator = self.teacher.calculate_average_of_classroom(classroom)
        self.assertCountEqual(list(generator), [{'Carlee Holloway': 8.0}, {'Jude Arroyo': 8.0}])

    def test_calculate_average_of_classroom_with_invalid_teacher(self):
        classroom = Classroom(Teacher('Selena Francis'))
        classroom.add_student(julia)
        error_message = 'This teacher can not correct for classroom of Selena Francis with 1 students'
        with self.assertRaises(BaseException) as context:
            self.teacher.calculate_average_of_classroom(classroom)

        self.assertTrue(error_message in str(context.exception))
