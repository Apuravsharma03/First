import random   # import used to shuffle the questions

# ----- CLASS -----
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.upper() == self.answer.upper()


# ----- FUNCTION to ask a single question -----
def ask_question(question_obj):
    print("\n" + question_obj.text)
    for option in question_obj.options:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ")
    return question_obj.check_answer(user_answer)  # function used to check answer


# ----- FUNCTION to play the full quiz -----
def play_quiz(questions):
    score = 0
    random.shuffle(questions)  # shuffle questions so game is different every time
    
    # for loop to go through all questions
    for q in questions:
        if ask_question(q):   # function used here
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! The correct answer was:", q.answer)
    
    print("\nYour final score:", score, "/", len(questions))


# ----- MAIN PROGRAM -----
if __name__ == "__main__":  # main stuff
    # list of questions (each is an object of class Question)
    questions = [
        Question("What is the capital of France?",
                 ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"], "A"),
        
        Question("Which planet is known as the Red Planet?",
                 ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "B"),
        
        Question("What is 5 + 7?",
                 ["A. 10", "B. 12", "C. 14", "D. 15"], "B"),
        
        Question("Which language is used for AI?",
                 ["A. Python", "B. Hindi", "C. Spanish", "D. JavaScript"], "A"),
        
        Question("Who developed the theory of relativity?",
                 ["A. Newton", "B. Einstein", "C. Galileo", "D. Tesla"], "B")
    ]

    # while loop to allow replay
    while True:
        play_quiz(questions)   # function used here
        again = input("\nDo you want to play again? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks for playing! 👋")
            break
