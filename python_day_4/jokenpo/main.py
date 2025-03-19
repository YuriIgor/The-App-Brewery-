import random
from figures import rock_fig, paper_fig, scissors_fig

rock = 1
paper = 2
scissors = 3

player_score = 0
computer_score = 0

print("Welcome to Jokenpo!")
print("You're about to play against the computer.")

game_on = True
while game_on == True:

    print("You can type 0 to exit.")
    choice = input("Choose rock, paper or scissors:\n").lower()
    if choice == "0":
        print(f"Your score: {player_score}.")
        print(f"Computer score: {computer_score}.")
        print("Ok, bye.")
        game_on = False
    elif choice == "rock":
        print(rock_fig)
    elif choice == "paper":
        print(paper_fig)
    elif choice == "scissors":
        print(scissors_fig)
    else:
        print("Invalid input.")
    
    computer_choice = random.randint(1, 3)
    if computer_choice == 1 and choice == "rock":
        print("Computer chooses:")
        print(rock_fig)
        print("DRAW!")
    elif computer_choice == 2 and choice == "rock":
        print("Computer chooses:")
        print(paper_fig)
        print("Computer Wins!")
        computer_score += 1
    elif computer_choice == 3 and choice == "rock":
        print("Computer chooses:")
        print(scissors_fig)
        print("You Win!")
        player_score += 1
    elif computer_choice == 1 and choice == "paper":
        print("Computer chooses:")
        print(rock_fig)
        print("You Win!")
        player_score += 1
    elif computer_choice == 2 and choice == "paper":
        print("Computer chooses:")
        print(paper_fig)
        print("DRAW!")
    elif computer_choice == 3 and choice == "paper":
        print("Computer chooses:")
        print(scissors_fig)
        print("Computer Wins!")
        computer_score += 1
    elif computer_choice == 1 and choice == "scissors":
        print("Computer chooses:")
        print(rock_fig)
        print("Computer Wins!")
        computer_score += 1
    elif computer_choice == 2 and choice == "scissors":
        print("Computer chooses:")
        print(paper_fig)
        print("You Win!")
        player_score += 1
    elif computer_choice == 3 and choice == "scissors":
        print("Computer chooses:")
        print(scissors_fig)
        print("DRAW!")



