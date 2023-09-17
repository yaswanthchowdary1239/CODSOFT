import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer multiple-choice or fill-in-the-blank questions.")
        print("Let's start!\n")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for idx, question in enumerate(self.questions, start=1):
            print(f"Question {idx}: {question['question']}")
            for choice in question['choices']:
                print(choice)
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_user_answer(user_answer, question['answer'])
            print()

    def evaluate_user_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {correct_answer}\n")

    def display_final_results(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")
        if self.score == len(self.questions):
            print("Congratulations! You got all the questions right!")
        elif self.score >= len(self.questions) // 2:
            print("Good job! You did well.")
        else:
            print("Keep practicing to improve your score.")

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        return play_again == 'yes'

# Sample quiz questions
quiz_questions = [
    {
        'question': "What is the capital of France?",
        'choices': ["A) London", "B) Paris", "C) Berlin", "D) Rome"],
        'answer': "b"
    },
    {
        'question': "Who wrote the play 'Romeo and Juliet'?",
        'choices': ["A) Mark Twain", "B) William Shakespeare", "C) Jane Austen", "D) Charles Dickens"],
        'answer': "b"
    }
    # Add more questions here
]

def main():
    while True:
        game = QuizGame(quiz_questions)
        game.display_welcome_message()
        game.present_quiz_questions()
        game.display_final_results()

        if not game.play_again():
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
