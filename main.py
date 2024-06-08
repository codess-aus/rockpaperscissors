# Create a rock, paper, scissors game where the user plays against the computer.
# The computer randomly generates a choice and the user inputs their choice.
# The program then compares the two choices and determines the winner.
# The game is won by the player who wins the best of 3 rounds.
# make the code as pythonic as possible

# Import the random module to generate random choices for the computer
import random

# Function to get the user's choice
def get_user_choice():
    # Prompt the user to enter their choice
    user_choice = input("Enter your choice: rock, paper, or scissors: ")
    # Return the user's choice
    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    # The computer randomly chooses from rock, paper, or scissors
    computer_choice = random.choice(["rock", "paper", "scissors"])
    # Return the computer's choice
    return computer_choice

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    # If the user's choice is the same as the computer's, it's a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # If the user chooses rock and the computer chooses scissors, the user wins
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    # If the user chooses scissors and the computer chooses paper, the user wins
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    # If the user chooses paper and the computer chooses rock, the user wins
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    # In all other cases, the computer wins
    else:
        return "Computer wins!"
    
# Main function to run the game
def main():
    # Initialize scores for the user and the computer
    user_score = 0
    computer_score = 0
    # Continue the game until either the user or the computer has 2 points
    while user_score < 2 and computer_score < 2:
        # Get the user's and the computer's choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        # Print the computer's choice
        print(f"Computer chose: {computer_choice}")
        # Print the result of the game
        print(determine_winner(user_choice, computer_choice))
        # If the user wins, increment the user's score
        if determine_winner(user_choice, computer_choice) == "You win!":
            user_score += 1
        # If the computer wins, increment the computer's score
        elif determine_winner(user_choice, computer_choice) == "Computer wins!":
            computer_score += 1
        # Print the current scores
        print(f"User score: {user_score}, Computer score: {computer_score}")
    # If the user's score is 2, the user wins the game
    if user_score == 2:
        print("You win the game!")
    # Otherwise, the computer wins the game
    else:
        print("Computer wins the game!")

# If this script is run directly (not imported), start the game
if __name__ == "__main__":
    main()