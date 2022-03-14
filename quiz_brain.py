class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {current_question.text} True or false?: ")
        self.check_answer (user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are correct!")
        else:
            print("Your answer is incorrect.")
        print(f"The answer was {correct_answer}.")
        print(f"Your score is: {self.score} out of {self.question_number}.")