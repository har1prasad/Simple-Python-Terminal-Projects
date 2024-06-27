from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    qns_txt = i["text"]
    ans = i["answer"]
    new_question = Question(qns_txt, ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score is: {quiz.score}/{quiz.question_number}")

