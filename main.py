from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []

# write a for loop to iterate over the question data
for entry in question_data:
    question_text = entry["question"]
    question_answer = entry["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n\nYou've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
