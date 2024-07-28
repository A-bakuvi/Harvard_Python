from project import determine_winner, display_scores
import pytest

def test_determine_winner():
    determine_winner("scissors", "paper") == "You win!"
    determine_winner("rock", "paper") == "Computer wins!"
    determine_winner("paper", "paper") == "It's a tie!"

def test_display_scores():
    display_scores(1,0) == "Your score: 1, Computer's score: 0"
    display_scores(1,2) == "Your score: 1, Computer's score: 2"
    display_scores(1,3) == "Your score: 1, Computer's score: 3"
    