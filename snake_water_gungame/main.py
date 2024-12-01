import random

'''
Game Rules:
s for snake -> 1
w for water -> -1
g for gun -> 0
'''

def play_game():
    while True:
        computer = random.choice([1, -1, 0])
        your_dict = {"s": 1, "w": -1, "g": 0}
        reverse_dict = {1: "snake", -1: "water", 0: "gun"}

        # Take user input and validate it
        yourchoice = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

        if yourchoice not in your_dict:
            print("Invalid input! Please enter 's', 'w', or 'g'.")
            continue

        you = your_dict[yourchoice]

        # Display choices
        print(f"You : {reverse_dict[you]}\n Bot : {reverse_dict[computer]}")

        # Determine the winner
        if computer == you:
            print("It's a Draw!")
        else:
            if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
                print("Congrats! You won!")
            else:
                print("You lost!!!")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
