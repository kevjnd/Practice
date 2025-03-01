import random

class RiddleGame:
    def __init__(self):
        # List of riddles and answers
        self.riddles = [
            {
                "question": "I am light as a feather, yet the strongest man can't hold me for much longer. What am I?",
                "answer": "breath"
            },
            {
                "question": "What is always in front of you but can't be seen?",
                "answer": "future"
            },
            {
                "question": "I can talk, but I don't have a mouth. I can listen, but I don't have ears. What am I?",
                "answer": "telephone"
            },
            {
                "question": "I am always hungry, but I never eat. I drink a lot, but never thirst. What am I?",
                "answer": "fire"
            },
            {
                "question": "I can't move, but I always move forward. What am I?",
                "answer": "time"
            }
        ]
        self.score = 0

    def ask_riddle(self):
        riddle = random.choice(self.riddles)  # Choose a random riddle
        print(f"Try to solve this riddle:\nRiddle: {riddle['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == riddle["answer"]:
            print("Correct answer! Well done!")
            self.score += 1
        else:
            print(f"Incorrect answer! The correct answer is: {riddle['answer']}")
            self.provide_options(riddle)

    def provide_options(self, riddle):
        print("\nWhat would you like to do next?")
        print("1. Try again")
        print("2. Skip this riddle")
        print("3. Show the correct answer")
        choice = input("Enter the number of your choice (1/2/3): ").strip()

        if choice == "1":
            print("Let's try again!\n")
            self.ask_riddle()
        elif choice == "2":
            print("You skipped the riddle.\n")
        elif choice == "3":
            print(f"The correct answer was: {riddle['answer']}\n")
        else:
            print("Invalid choice. Skipping the riddle.\n")

    def start_game(self):
        print("Welcome to the Riddle Game! Try to solve as many riddles as you can.")
        while True:
            self.ask_riddle()
            play_again = input("Do you want to continue playing? (yes/no): ").strip().lower()
            if play_again != "yes":
                print(f"Game over. Your final score is: {self.score}")
                break

if __name__ == "__main__":
    game = RiddleGame()
    game.start_game()