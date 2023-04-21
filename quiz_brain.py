class QuizBrain:
    def __init__(self,list):
        self.question_no=0
        self.question_list=list
        self.score=0
    def still_has_question(self):
        return self.question_no<len(self.question_list)
        #     return True
        # else:
        #     return False
    def check_answer(self,user_ans,correct_ans):
        if(user_ans==correct_ans):
            print("You got it Right!!!")
            self.score+=1
        else:
            print("That's Wrong !!!")
        print(f"The correct answer was : {correct_ans} .")
        print(f"Your current score is : {self.score}/{self.question_no}")
        print("\n")
    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_ans=input(f"Q{self.question_no} : {current_question.text} (True/False) :\n")
        self.check_answer(user_ans,current_question.answer)
