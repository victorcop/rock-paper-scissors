"""Rock Paper Scissors game logic."""

import logging
import random
import sys
from typing import Dict, List, Literal, Tuple

import questionary

# Type alias for valid choices
Choice = Literal["rock", "paper", "scissors"]

# Game configuration
VALID_CHOICES: List[str] = ["rock", "paper", "scissors"]
WIN_CONDITIONS: Dict[str, str] = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

# Setup logger
logger = logging.getLogger(__name__)


def get_computer_choice() -> Choice:
    """
    Randomly select between 'rock', 'paper', or 'scissors' for the computer's choice.

    Returns:
        Choice: The computer's randomly selected choice.
    """
    choice = random.choice(VALID_CHOICES)
    logger.debug(f"Computer selected: {choice}")
    return choice  # type: ignore


def get_user_choice(prompt: bool = True, interactive: bool = True) -> Choice:
    """
    Get the user's choice of 'rock', 'paper', or 'scissors'.

    Args:
        prompt: Whether to display the input prompt.
        interactive: Whether to use interactive menu (Azure CLI style).

    Returns:
        Choice: The user's validated choice.
    """
    # Check if we're in an interactive terminal (not piped input)
    is_tty = sys.stdin.isatty()

    # Use interactive menu if available and requested
    if interactive and is_tty and prompt:
        try:
            choice = questionary.select(
                "Select your choice:",
                choices=[
                    questionary.Choice("1. 🪨 Rock", value="rock"),
                    questionary.Choice("2. 📄 Paper", value="paper"),
                    questionary.Choice("3. ✂️  Scissors", value="scissors"),
                ],
                style=questionary.Style(
                    [
                        ("highlighted", "fg:cyan bold"),
                        ("pointer", "fg:cyan bold"),
                    ]
                ),
            ).ask()

            if choice is None:  # User pressed Ctrl+C
                raise KeyboardInterrupt

            logger.debug(f"User selected: {choice}")
            return choice  # type: ignore
        except (KeyboardInterrupt, EOFError):
            raise
        except Exception as e:
            logger.warning(f"Interactive menu failed: {e}, falling back to text input")
            # Fall through to text input

    # Fallback to text input for non-interactive or piped input
    if prompt:
        user_input = (
            input("Enter your choice (rock, paper, scissors): ").strip().lower()
        )
    else:
        user_input = input().strip().lower()

    while user_input not in VALID_CHOICES:
        logger.warning(f"Invalid choice received: '{user_input}'")
        print("Invalid choice. Please try again.")
        user_input = (
            input("Enter your choice (rock, paper, scissors): ").strip().lower()
        )

    logger.debug(f"User selected: {user_input}")
    return user_input  # type: ignore


def determine_winner(user_choice: Choice, computer_choice: Choice) -> str:
    """
    Determine the winner of the game based on user and computer choices.

    Args:
        user_choice: The user's choice ('rock', 'paper', or 'scissors').
        computer_choice: The computer's choice ('rock', 'paper', or 'scissors').

    Returns:
        str: A string indicating the result: "You win!", "You lose!", or "It's a tie!"
    """
    logger.debug(f"Comparing: user={user_choice} vs computer={computer_choice}")

    if user_choice == computer_choice:
        logger.info("Game result: Tie")
        return "It's a tie!"
    elif WIN_CONDITIONS[user_choice] == computer_choice:
        logger.info("Game result: User wins")
        return "You win!"
    else:
        logger.info("Game result: Computer wins")
        return "You lose!"


def play_game(verbose: bool = False) -> Tuple[Choice, Choice, str]:
    """
    Play a single game of Rock, Paper, Scissors.

    Args:
        verbose: Whether to print game information to console.

    Returns:
        Tuple[Choice, Choice, str]: User choice, computer choice, and result message.
    """
    logger.info("Starting new game")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    if verbose:
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
    else:
        print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    logger.info(f"Game completed: {user_choice} vs {computer_choice} -> {result}")
    return user_choice, computer_choice, result


def play_multiple_rounds(rounds: int, verbose: bool = False) -> Dict[str, int]:
    """
    Play multiple rounds of Rock, Paper, Scissors and track scores.

    Args:
        rounds: Number of rounds to play.
        verbose: Whether to print detailed game information.

    Returns:
        Dict[str, int]: Score dictionary with 'user', 'computer', and 'ties' counts.
    """
    logger.info(f"Starting game session with {rounds} rounds")

    score: Dict[str, int] = {"user": 0, "computer": 0, "ties": 0}

    print(f"\n{'='*50}")
    print(f"Playing {rounds} round{'s' if rounds > 1 else ''}")
    print(f"{'='*50}\n")

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}/{rounds}")
        print("-" * 30)

        user_choice, computer_choice, result = play_game(verbose)

        # Update score
        if "win" in result.lower():
            score["user"] += 1
        elif "lose" in result.lower():
            score["computer"] += 1
        else:
            score["ties"] += 1

        # Show current score
        print(
            f"\nCurrent Score - You: {score['user']} | Computer: {score['computer']} | Ties: {score['ties']}"
        )

        if round_num < rounds:
            print()  # Blank line between rounds

    # Final summary
    print(f"\n{'='*50}")
    print("GAME OVER - Final Score")
    print(f"{'='*50}")
    print(f"You: {score['user']}")
    print(f"Computer: {score['computer']}")
    print(f"Ties: {score['ties']}")

    # Determine overall winner
    if score["user"] > score["computer"]:
        print("\n🎉 You won the game!")
        logger.info(
            f"Game session completed: User wins ({score['user']}-{score['computer']})"
        )
    elif score["computer"] > score["user"]:
        print("\n💻 Computer won the game!")
        logger.info(
            f"Game session completed: Computer wins ({score['computer']}-{score['user']})"
        )
    else:
        print("\n🤝 It's a tie overall!")
        logger.info(
            f"Game session completed: Tie ({score['user']}-{score['computer']})"
        )

    print(f"{'='*50}\n")

    return score
