from question_model import Question
from data import generate_question_answer
from quiz_brain import QuizBrain
from ui import AppInterface


question_bank = []
for question in range(20):
    question_text, question_answer = generate_question_answer()
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
quiz_game_ui = AppInterface(quiz_brain)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
