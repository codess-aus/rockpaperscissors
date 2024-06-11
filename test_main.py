import unittest
from unittest.mock import patch
from main import get_computer_choice, determine_winner, Choice, VALID_CHOICES, WIN_MESSAGE, LOSE_MESSAGE, TIE_MESSAGE, main

class TestMain(unittest.TestCase):
    def test_get_computer_choice(self):
        """Test that get_computer_choice returns a valid choice."""
        choice = get_computer_choice()
        self.assertIn(choice, VALID_CHOICES)

    def test_determine_winner(self):
        """Test that determine_winner correctly determines the winner."""
        self.assertEqual(determine_winner(Choice.ROCK.value, Choice.SCISSORS.value), WIN_MESSAGE)
        self.assertEqual(determine_winner(Choice.PAPER.value, Choice.ROCK.value), WIN_MESSAGE)
        self.assertEqual(determine_winner(Choice.SCISSORS.value, Choice.PAPER.value), WIN_MESSAGE)
        self.assertEqual(determine_winner(Choice.ROCK.value, Choice.PAPER.value), LOSE_MESSAGE)
        self.assertEqual(determine_winner(Choice.PAPER.value, Choice.SCISSORS.value), LOSE_MESSAGE)
        self.assertEqual(determine_winner(Choice.SCISSORS.value, Choice.ROCK.value), LOSE_MESSAGE)
        self.assertEqual(determine_winner(Choice.ROCK.value, Choice.ROCK.value), TIE_MESSAGE)
        self.assertEqual(determine_winner(Choice.PAPER.value, Choice.PAPER.value), TIE_MESSAGE)
        self.assertEqual(determine_winner(Choice.SCISSORS.value, Choice.SCISSORS.value), TIE_MESSAGE)

    @patch('builtins.input', side_effect=[Choice.ROCK.value, Choice.PAPER.value, Choice.SCISSORS.value])
    @patch('main.get_computer_choice', side_effect=[Choice.SCISSORS.value, Choice.ROCK.value, Choice.PAPER.value])
    def test_main(self, mock_get_computer_choice, mock_input):
        """Test the main function."""
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("You win the game!")

if __name__ == "__main__":
    unittest.main()