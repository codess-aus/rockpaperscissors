import random

# Define constants for the choices and winning combinations
CHOICES = ['rock', 'paper', 'scissors']
WINNING_COMBINATIONS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

class RockPaperScissorsGame:
    def __init__(self):
        """Initialize the game state."""
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        """Prompt the user for their choice and return it."""
        return input(f"Enter {', '.join(CHOICES)}: ")

    def get_computer_choice(self):
        """Return the computer's choice, selected randomly."""
        return random.choice(CHOICES)

    def determine_winner(self, user_choice, computer_choice):
        """
        Determine the winner based on the user's and computer's choices.
        Return 'user', 'computer', or 'tie'.
        """
        if user_choice == computer_choice:
            return "tie"
        elif WINNING_COMBINATIONS[user_choice] == computer_choice:
            return "user"
        else:
            return "computer"

    def update_scores(self, winner):
        """Update the scores based on the winner."""
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def print_round_results(self, user_choice, computer_choice, winner):
        """Print the results of the round."""
        print(f"User chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if winner == "user":
            print("User wins this round!")
        elif winner == "computer":
            print("Computer wins this round!")
        else:
            print("This round is a tie!")

    def declare_champion(self):
        """Declare the champion based on the scores."""
        if self.user_score > self.computer_score:
            print("User is the champion!")
        else:
            print("Computer is the champion!")

    def play(self):
        """Play the game until either the user or the computer has won 2 rounds."""
        while self.user_score < 2 and self.computer_score < 2:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)
            self.update_scores(winner)
            self.print_round_results(user_choice, computer_choice, winner)
        self.declare_champion()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
