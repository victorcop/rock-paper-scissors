"""Rock Paper Scissors - A simple command-line game."""

from rock_paper_scissors.rock_paper_scissors import (
    Choice,
    determine_winner,
    get_computer_choice,
    get_user_choice,
    play_game,
    play_multiple_rounds,
    VALID_CHOICES,
    WIN_CONDITIONS,
)

__version__ = "1.0.0"
__all__ = [
    'Choice',
    'play_game',
    'play_multiple_rounds',
    'get_computer_choice',
    'get_user_choice',
    'determine_winner',
    'VALID_CHOICES',
    'WIN_CONDITIONS',
]