# Create a rock, paper, scissors game where the user plays against the computer.
# The computer randomly generates a choice and the user inputs their choice.
# The program then compares the two choices and determines the winner.
# The game is won by the player who wins the best of 3 rounds.
# make the code as pythonic as possible

import random
from enum import Enum

class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

VALID_CHOICES = [c.value for c in Choice]
WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "Computer wins!"
TIE_MESSAGE = "It's a tie!"
GAME_RULES = {
    Choice.ROCK.value: Choice.SCISSORS.value,
    Choice.PAPER.value: Choice.ROCK.value,
    Choice.SCISSORS.value: Choice.PAPER.value
}

def get_user_choice():
    """Prompt the user for their choice until they enter a valid one.
    
    Returns:
        str: The user's choice.
    """
    user_choice = ""
    while user_choice not in VALID_CHOICES:
        user_choice = input("Enter your choice: rock, paper, or scissors: ")
        if user_choice not in VALID_CHOICES:
            print("Invalid choice. Please enter rock, paper, or scissors.")
    return user_choice

def get_computer_choice():
    """Get the computer's choice.
    
    Returns:
        str: The computer's choice, selected randomly.
    """
    return random.choice(VALID_CHOICES)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of a round.
    
    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
    
    Returns:
        str: A message indicating the result of the round.
    """
    if user_choice == computer_choice:
        return TIE_MESSAGE
    if GAME_RULES[user_choice] == computer_choice:
        return WIN_MESSAGE
    return LOSE_MESSAGE

def main():
    """Run the main game loop."""
    user_score = 0
    computer_score = 0
    while user_score < 2 and computer_score < 2:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        if result == WIN_MESSAGE:
            user_score += 1
        elif result == LOSE_MESSAGE:
            computer_score += 1
        print(f"Computer chose: {computer_choice}")
        print(result)
        print(f"User score: {user_score}, Computer score: {computer_score}")
    if user_score == 2:
        print("You win the game!")
    else:
        print("Computer wins the game!")

if __name__ == "__main__":
  main()

