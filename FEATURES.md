# Enhanced Features Guide

This document describes the enhanced features added to the Rock Paper Scissors project.

## Type Hints

All functions now include complete type annotations using Python 3.7+ type hints:

```python
from typing import Dict, List, Literal, Tuple

Choice = Literal['rock', 'paper', 'scissors']

def determine_winner(user_choice: Choice, computer_choice: Choice) -> str:
    """Determine the winner with type-safe parameters."""
    ...

def play_multiple_rounds(rounds: int, verbose: bool = False) -> Dict[str, int]:
    """Play multiple rounds and return score dictionary."""
    ...
```

### Benefits:
- Static type checking with `mypy`
- Better IDE autocomplete and IntelliSense
- Self-documenting code
- Catch type errors before runtime

## Logging

The game now uses Python's built-in `logging` module instead of print statements for internal operations:

```python
import logging

logger = logging.getLogger(__name__)

logger.debug("Computer selected: rock")
logger.info("Game result: User wins")
logger.warning("Invalid choice received: 'rokc'")
```

### Logging Levels:

- **Default (WARNING)**: Only errors and warnings
- **Verbose (INFO)**: General game flow information
  ```bash
  rock-paper-scissors -v
  ```
- **Debug (DEBUG)**: Detailed debugging information
  ```bash
  rock-paper-scissors --debug
  ```

### Example Debug Output:

```bash
$ rock-paper-scissors --debug
2025-11-05 10:30:45 - __main__ - INFO - Starting single round game
2025-11-05 10:30:47 - rock_paper_scissors - DEBUG - User selected: rock
2025-11-05 10:30:47 - rock_paper_scissors - DEBUG - Computer selected: scissors
2025-11-05 10:30:47 - rock_paper_scissors - DEBUG - Comparing: user=rock vs computer=scissors
2025-11-05 10:30:47 - rock_paper_scissors - INFO - Game result: User wins
```

## Command-Line Interface (CLI)

### Argument Parsing

The game now uses `argparse` for professional command-line argument handling:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='rock-paper-scissors',
    description='Play Rock, Paper, Scissors game against the computer'
)
```

### Available Options

#### `-r, --rounds N`
Play multiple rounds with score tracking:

```bash
# Play 3 rounds
rock-paper-scissors -r 3

# Play 10 rounds
rock-paper-scissors --rounds 10
```

**Features:**
- Tracks wins, losses, and ties
- Displays current score after each round
- Shows final summary with overall winner
- Validates that rounds >= 1

#### `-v, --verbose`
Enable verbose output to see more game details:

```bash
rock-paper-scissors -v

# Output shows:
# You chose: rock
# Computer chose: scissors
# You win!
```

Without verbose, only the computer's choice and result are shown.

#### `--debug`
Enable detailed debug logging for development:

```bash
rock-paper-scissors --debug
```

Shows:
- Function calls and returns
- User input validation
- Random choice generation
- Winner determination logic

#### `--version`
Display version information:

```bash
rock-paper-scissors --version
# Output: rock-paper-scissors 1.0.0
```

#### `-h, --help`
Show help message with all options:

```bash
rock-paper-scissors --help
```

### Combining Options

You can combine multiple options:

```bash
# Play 5 rounds with verbose output and debug logging
rock-paper-scissors -r 5 -v --debug

# Play 3 rounds with just verbose output
rock-paper-scissors --rounds 3 --verbose
```

## Multiple Rounds Feature

### Basic Multi-Round Game

```bash
rock-paper-scissors -r 5
```

**Output:**
```
==================================================
Playing 5 rounds
==================================================

Round 1/5
------------------------------
Enter your choice (rock, paper, scissors): rock
Computer chose: scissors
You win!

Current Score - You: 1 | Computer: 0 | Ties: 0

Round 2/5
------------------------------
Enter your choice (rock, paper, scissors): paper
Computer chose: rock
You win!

Current Score - You: 2 | Computer: 0 | Ties: 0

...

==================================================
GAME OVER - Final Score
==================================================
You: 3
Computer: 1
Ties: 1

🎉 You won the game!
==================================================
```

### Score Tracking

The `play_multiple_rounds()` function returns a score dictionary:

```python
score = play_multiple_rounds(5)
# Returns: {'user': 3, 'computer': 1, 'ties': 1}
```

### Winner Determination

After all rounds:
- **User wins** if `score['user'] > score['computer']` → 🎉
- **Computer wins** if `score['computer'] > score['user']` → 💻
- **Tie** if `score['user'] == score['computer']` → 🤝

## Configuration Constants

Game configuration is now centralized:

```python
# Valid choices
VALID_CHOICES: List[str] = ['rock', 'paper', 'scissors']

# Win conditions (key beats value)
WIN_CONDITIONS: Dict[str, str] = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
```

**Benefits:**
- Easy to modify game rules
- Single source of truth
- Testable configuration

## Input Normalization

User input is now normalized automatically:

```python
user_input = input().strip().lower()
```

**Accepts:**
- `"rock"` → `"rock"`
- `"ROCK"` → `"rock"`
- `"  Rock  "` → `"rock"`
- `"PaPeR"` → `"paper"`

## Error Handling

### Invalid Rounds

```bash
$ rock-paper-scissors -r 0
Error: Number of rounds must be at least 1
```

### Keyboard Interrupt (Ctrl+C)

```bash
$ rock-paper-scissors
Enter your choice: ^C

Game interrupted by user. Goodbye!
```

Returns exit code 130 (standard for SIGINT).

### Unexpected Errors

All unexpected errors are caught and logged:

```bash
An error occurred: <error message>
```

Returns exit code 1.

## API Usage

You can also use the game as a Python library:

```python
from rock_paper_scissors import play_game, play_multiple_rounds

# Play a single game programmatically
user_choice, computer_choice, result = play_game(verbose=True)

# Play multiple rounds
score = play_multiple_rounds(rounds=5, verbose=False)
print(f"Final score: {score}")
```

## Testing

The enhanced features include comprehensive tests:

- **33 total tests** (up from 12)
- Type hint validation
- CLI argument parsing tests
- Multi-round functionality tests
- Input normalization tests
- Error handling tests
- Logging setup tests

Run tests:
```bash
python -m unittest discover tests -v
```

## Summary

### What Was Added:

✅ **Type Hints** - Complete type annotations throughout
✅ **Logging** - Professional logging instead of debug prints
✅ **CLI Arguments** - Full argparse implementation
✅ **Multiple Rounds** - Score tracking across rounds
✅ **Input Normalization** - Case-insensitive, trimmed input
✅ **Error Handling** - Graceful handling of errors and interrupts
✅ **Configuration** - Centralized game constants
✅ **Enhanced Tests** - Comprehensive test coverage

### Lines of Code:

- **Before**: ~30 lines
- **After**: ~250 lines (game logic + CLI)
- **Tests**: ~200 lines (33 tests)
- **Total**: ~450 lines of production-quality code

This simple game now demonstrates professional Python development practices! 🎮✨
