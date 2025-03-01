import random

class RiddleGame:
    def __init__(self):
        # List of riddles and answers
        self.riddles = [
            {
                "question": "I am light as a feather, yet the strongest man can't hold me for much longer. What am I?",
                "answer": "breath",
                "hint": "It's something you do to stay alive."
            },
            {
                "question": "What is always in front of you but can't be seen?",
                "answer": "future",
                "hint": "It's the time that is yet to come."
            },
            {
                "question": "I can talk, but I don't have a mouth. I can listen, but I don't have ears. What am I?",
                "answer": "telephone",
                "hint": "You use it to communicate."
            },
            {
                "question": "I am always hungry, but I never eat. I drink a lot, but never thirst. What am I?",
                "answer": "fire",
                "hint": "It can be dangerous if not controlled."
            },
            {
                "question": "I can't move, but I always move forward. What am I?",
                "answer": "time",
                "hint": "It keeps ticking even if you don't notice."
            },
            {
                "question": "The more of this there is, the less you see. What is it?",
                "answer": "darkness",
                "hint": "It's the opposite of light."
            },
            {
                "question": "What has keys but can't open locks?",
                "answer": "piano",
                "hint": "It makes sound when played."
            },
            {
                "question": "What has a head, a tail, but no body?",
                "answer": "coin",
                "hint": "It's something you flip."
            },
            {
                "question": "What can travel around the world while staying in the corner?",
                "answer": "stamp",
                "hint": "It sticks to something to help it travel."
            },
            {
                "question": "I am tall when I am young, and I am short when I am old. What am I?",
                "answer": "candle",
                "hint": "I provide light."
            },
            {
                "question": "What has a heart that doesn't beat?",
                "answer": "artichoke",
                "hint": "It's a vegetable."
            },
            {
                "question": "The more you take, the more you leave behind. What am I?",
                "answer": "footsteps",
                "hint": "You leave these when you walk."
            },
            {
                "question": "What comes down but never goes up?",
                "answer": "rain",
                "hint": "It falls from the sky."
            },
            {
                "question": "What can be cracked, made, told, and played?",
                "answer": "joke",
                "hint": "It makes people laugh."
            },
            {
                "question": "What has one eye but can't see?",
                "answer": "needle",
                "hint": "It's used in sewing."
            },
            {
                "question": "What begins with T, ends with T, and has T in it?",
                "answer": "teapot",
                "hint": "You use this to make tea."
            },
            {
                "question": "What is full of holes but still holds a lot of weight?",
                "answer": "sieve",
                "hint": "You use it in cooking to strain liquids."
            },
            {
                "question": "What has hands but can't clap?",
                "answer": "clock",
                "hint": "It helps you keep track of time."
            },
            {
                "question": "What has a neck but no head?",
                "answer": "bottle",
                "hint": "You can fill it with liquids."
            },
            {
                "question": "What can you catch but not throw?",
                "answer": "cold",
                "hint": "It makes you feel unwell."
            }
        ]
        self.score = 0

    def ask_riddle(self):
        riddle = random.choice(self.riddles)  # Chooses a random riddle
        print(f"Try to solve this riddle:\nRiddle: {riddle['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == riddle["answer"]:
            print("Correct answer! Well done!")
            self.score += 1
        else:
            print(f"Incorrect answer!")
            self.provide_options(riddle)

    def provide_options(self, riddle):
        print("\nWhat would you like to do next?")
        print("1. Try again")
        print("2. Skip this riddle")
        print("3. Show the correct answer")
        print("4. Get a hint")
        choice = input("Enter the number of your choice (1/2/3/4): ").strip()

        if choice == "1":
            print("Let's try again!\n")
            self.ask_riddle()
        elif choice == "2":
            print("You skipped the riddle.\n")
        elif choice == "3":
            print(f"The correct answer was: {riddle['answer']}\n")
        elif choice == "4":
            print(f"Hint: {riddle['hint']}\n")
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).\n")

    def start_game(self):
        print("Welcome to the Riddle Game! Try to solve as many riddles as you can.")
        while True:
            self.ask_riddle()
            play_again = input("Do you want to continue playing? (yes/y or no/n, type 'exit' to quit): ").strip().lower()

            if play_again == "exit":
                print(f"Game over. Your final score is: {self.score}")
                break
            elif play_again in ["yes", "y"]:
                continue
            elif play_again in ["no", "n"]:
                print(f"Game over. Your final score is: {self.score}")
                break
            else:
                print("Invalid input. To exit, type 'exit', or to continue, type 'yes/y' or 'no/n'.\n")

if __name__ == "__main__":
    game = RiddleGame()
    game.start_game()