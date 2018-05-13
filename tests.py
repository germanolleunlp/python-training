from src.teacher import Teacher
from src.classroom import Classroom
from src.student import Student
from src.quiz import Quiz
from src.question import Question
from src.student_answer import StudentAnswer

leon = Teacher(name = 'Leon Lang')
jamie = Teacher(name = 'Jamie Sweeney')

jude = Student(name = 'Jude Arroyo')
carlee = Student(name = 'Carlee Holloway')
caiden = Student(name = 'Caiden Henderson')
earl = Student(name = 'Earl Christensen')

leon_classroom = Classroom(
  teacher = leon,
  students = (jude, carlee, caiden, earl)
)

jamie_classroom = Classroom(
  teacher = jamie,
  students = (jude, carlee, earl)
)

Question(
  text = "In which year did Maradona score a goal with his hand?",
  answer = 1986,
  options = (1983, 1986, 1988)
)

question_one = Question(
  text = 'What is the national sport in Japan?',
  answer = 'Sumo Wrestling',
  options = ('Judo', 'Baseball', 'Sumo Wrestling')
)

question_two = Question(
  text = 'How many minutes is a rugby match?',
  answer = 80,
  options = (70, 80, 90)
)

question_three = Question(
  text = 'Which car won Fernando Alonso his first tittle in Formula 1 with?',
  answer = 'Renault',
  options = ('Renault', 'Ford', 'Peugeot')
)

question_four = Question(
  text = 'In which sport can you win the Davis Cup?',
  answer = 'Tennis',
  options = ('Football', 'Racing', 'Tennis')
)

leon_quiz = Quiz(
  teacher = leon,
  questions = (question_one, question_two, question_three)
)

jamie_quiz = Quiz(
  teacher = jamie,
  questions = (question_one, question_two, question_three, question_four)
)
