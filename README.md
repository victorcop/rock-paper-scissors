# Rock Paper Scissors

[![CI Tests](https://github.com/victorcop/rock-paper-scissors/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/victorcop/rock-paper-scissors/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/github/stars/victorcop/rock-paper-scissors?style=social)](https://github.com/victorcop/rock-paper-scissors)

A simple command-line Rock, Paper, Scissors game implemented in Python.

## Description

This is a classic Rock, Paper, Scissors game where you play against the computer. The computer randomly selects its choice, and the winner is determined based on the traditional rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

## Installation

### Option 1: Using venv and requirements.txt (Recommended)

1. Clone this repository:
```bash
git clone https://github.com/victorcop/rock-paper-scissors.git
cd rock-paper-scissors
```

2. Create and activate a virtual environment:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in editable mode:
```bash
pip install -e .
```

### Option 2: Direct Installation from Source

1. Clone this repository:
```bash
git clone https://github.com/victorcop/rock-paper-scissors.git
cd rock-paper-scissors
```

2. Install the package:
```bash
pip install -e .
```

### Option 3: Using pip (when published)

```bash
pip install rock-paper-scissors
```

## Usage

### Basic Usage

Play a single round:

```bash
rock-paper-scissors
```

Or run it as a Python module:

```bash
python -m rock_paper_scissors
```

### Command-Line Options

```bash
rock-paper-scissors [OPTIONS]

Options:
  -h, --help            Show help message and exit
  -r N, --rounds N      Number of rounds to play (default: 1)
  -v, --verbose         Enable verbose output (shows more game details)
  --debug               Enable debug logging (shows all logging messages)
  --version             Show program version and exit
```

### Examples

**Play a single round (default):**
```bash
rock-paper-scissors
```

**Play 5 rounds with score tracking:**
```bash
rock-paper-scissors -r 5
```

**Play 3 rounds with verbose output:**
```bash
rock-paper-scissors --rounds 3 -v
```

**Enable debug logging to see detailed logs:**
```bash
rock-paper-scissors --debug
```

### How to Play

1. Run the game using one of the commands above
2. When prompted, select your choice:
   - **Interactive Mode** (default): Use arrow keys to navigate and Enter to select from:
     - 1. 🪨 Rock
     - 2. 📄 Paper
     - 3. ✂️  Scissors
   - **Text Mode** (piped input): Type your choice: `rock`, `paper`, or `scissors`
     - Input is case-insensitive: `ROCK`, `Rock`, or `rock` all work
     - Whitespace is automatically trimmed
3. The computer will make its choice
4. The winner will be announced!
5. If playing multiple rounds, scores are tracked and displayed after each round

### Features

- ✅ **Interactive Menu**: Azure CLI-style menu with arrow key navigation and emojis
- ✅ **Single or Multiple Rounds**: Play one round or multiple rounds with score tracking
- ✅ **Smart Input Detection**: Automatically detects interactive terminal vs piped input
- ✅ **Case-Insensitive Input**: Enter choices in any case (rock, ROCK, Rock)
- ✅ **Input Validation**: Invalid inputs are caught with helpful error messages
- ✅ **Score Tracking**: Keep track of wins, losses, and ties across multiple rounds
- ✅ **Logging Support**: Optional debug and verbose logging for development
- ✅ **Clean CLI**: Professional command-line interface with helpful options

## Development

### Project Structure

```
rock_paper_scissors/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── pr-checks.yml
│       ├── merge-to-main.yml
│       └── release.yml
├── src/
│   └── rock_paper_scissors/
│       ├── __init__.py
│       ├── __main__.py
│       └── rock_paper_scissors.py
├── tests/
│   ├── __init__.py
│   └── test_rock_paper_scissors.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

### Setting Up Development Environment

1. Clone the repository
2. Install in editable mode with dev dependencies:
```bash
pip install -e ".[dev]"
```

Or install test dependencies separately:
```bash
pip install pytest pytest-cov
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=rock_paper_scissors --cov-report=term-missing
```

Run tests with HTML coverage report:
```bash
pytest --cov=rock_paper_scissors --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_rock_paper_scissors.py
```

Run tests using unittest (no pytest required):
```bash
python -m unittest discover tests
```

### Running from Source

```bash
python -m src.rock_paper_scissors
```

## Requirements

- Python 3.8 or higher
- questionary >= 2.0.0 (for interactive menu)

### Development Requirements

- pytest >= 7.0.0 (for testing)
- pytest-cov >= 4.0.0 (for coverage reports)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on:

- How to set up your development environment
- Our branch strategy (feature branches → `dev` → `main`)
- How to submit pull requests
- Coding standards and guidelines
- Running tests

**Important**: All pull requests should target the `dev` branch, not `main`.

## Author

Victor Velasquez - vitorcop90@gmail.com
