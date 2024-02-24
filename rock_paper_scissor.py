# // take input from user
# // generate random choice
# // keep count, machine wins -1 , user wins +1, finally decide

import random

# Initialize win count and choices
count = 0
choices = ["rock", "paper", "scissors"]

# Define winning conditions
win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

# Game loop
for _ in range(3):
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(choices)
    print(f"You chose {player_choice}, computer chose {computer_choice}.")

    # Check for win, lose, and draw conditions
    if player_choice == computer_choice:
        print("It's a draw.")
    elif win_conditions[player_choice] == computer_choice:
        count += 1
        print("You win this round!")
    else:
        count -= 1
        print("You lose this round.")

# Determine and display the game outcome
if count > 0:
    print("You win!")
else:
    print("Computer Wins!")


   
        
    