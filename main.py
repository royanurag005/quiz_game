from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for item in question_data:
    each_question=Question(item["text"],item["answer"])
    question_bank.append(each_question)
# print(question_bank[0].text)

quiz=QuizBrain(question_bank)

count=0
while quiz.still_has_question():
    count+=1
    run=quiz.next_question()

print("End of Quiz !!!\n\n\nThank You!!!\n\n\n")
print(f"You final score was : {quiz.score}/{count}")
