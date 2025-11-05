# Contributing to Rock Paper Scissors

Thank you for considering contributing to this project! We welcome contributions from everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Branch Strategy](#branch-strategy)
- [Pull Request Process](#pull-request-process)
- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by a code of respect and professionalism. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed and what behavior you expected to see**
* **Include screenshots if applicable**
* **Include your Python version and operating system**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Explain why this enhancement would be useful**
* **List any alternative solutions you've considered**

### Contributing Code

We love pull requests! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch from `dev`
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass
6. Submit a pull request to the `dev` branch

## Development Workflow

### Branch Strategy

Our project uses a two-tier branching model:

```
main (production-ready code)
  ↑
  └── Pull Request from dev
       ↑
dev (integration branch)
  ↑
  ├── feature/your-feature-name
  ├── bugfix/issue-description
  └── enhancement/enhancement-name
```

#### Branch Descriptions

- **`main`**: Production-ready code. Only updated via pull requests from `dev`. Direct commits are not allowed.
- **`dev`**: Integration branch where all features are merged and tested together. All feature branches should branch from and merge back to `dev`.
- **`feature/*`**: New features or enhancements
- **`bugfix/*`**: Bug fixes
- **`hotfix/*`**: Critical fixes that need immediate attention (branch from `main`, merge to both `main` and `dev`)

### Creating a Feature Branch

Always branch from the latest `dev` branch:

```bash
# Update your local dev branch
git checkout dev
git pull origin dev

# Create your feature branch
git checkout -b feature/your-feature-name
```

### Branch Naming Conventions

Use descriptive branch names with the following prefixes:

- `feature/` - New features (e.g., `feature/add-score-tracking`)
- `bugfix/` - Bug fixes (e.g., `bugfix/fix-tie-logic`)
- `enhancement/` - Improvements to existing features (e.g., `enhancement/improve-input-validation`)
- `docs/` - Documentation updates (e.g., `docs/update-readme`)
- `test/` - Test additions or improvements (e.g., `test/add-integration-tests`)
- `refactor/` - Code refactoring (e.g., `refactor/simplify-winner-logic`)

## Pull Request Process

### Submitting a Pull Request

1. **Ensure your branch is up to date with `dev`**:
   ```bash
   git checkout dev
   git pull origin dev
   git checkout your-feature-branch
   git merge dev
   ```

2. **Run all tests and ensure they pass**:
   ```bash
   python -m unittest discover tests
   # or with pytest
   pytest
   ```

3. **Commit your changes** with clear, descriptive commit messages

4. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** targeting the `dev` branch (NOT `main`)

6. **Fill out the PR template** with:
   - Clear description of the changes
   - Reference to any related issues
   - Screenshots (if applicable)
   - Confirmation that tests pass

### Pull Request Requirements

Before your pull request can be merged, it must:

- ✅ Target the `dev` branch (unless it's a hotfix)
- ✅ Pass all existing tests
- ✅ Include new tests for new functionality
- ✅ Follow the project's coding standards
- ✅ Have a clear and descriptive title
- ✅ Include updated documentation if applicable
- ✅ Be reviewed and approved by at least one maintainer

### Pull Request Review Process

1. A maintainer will review your PR within a few days
2. Address any requested changes
3. Once approved, a maintainer will merge your PR into `dev`
4. Your changes will be included in the next release when `dev` is merged to `main`

### Release Process

Only maintainers can create releases:

1. Features are merged into `dev` throughout the development cycle
2. When ready for release, create a PR from `dev` → `main`
3. After thorough testing and review, merge to `main`
4. Tag the release on `main`
5. Merge `main` back to `dev` to keep branches in sync

## Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   cd rock-paper-scissors
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```

   Or install dependencies separately:
   ```bash
   pip install -e .
   pip install pytest pytest-cov
   ```

4. **Verify installation**:
   ```bash
   rock-paper-scissors
   ```

## Running Tests

### Using unittest (no dependencies required)

```bash
# Run all tests
python -m unittest discover tests

# Run with verbose output
python -m unittest discover tests -v

# Run specific test file
python -m unittest tests.test_rock_paper_scissors

# Run specific test class
python -m unittest tests.test_rock_paper_scissors.TestDetermineWinner

# Run specific test method
python -m unittest tests.test_rock_paper_scissors.TestDetermineWinner.test_user_wins_scenarios
```

### Using pytest (recommended)

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=rock_paper_scissors --cov-report=term-missing

# Run with HTML coverage report
pytest --cov=rock_paper_scissors --cov-report=html

# Run specific test file
pytest tests/test_rock_paper_scissors.py

# Run specific test class
pytest tests/test_rock_paper_scissors.py::TestDetermineWinner

# Run specific test method
pytest tests/test_rock_paper_scissors.py::TestDetermineWinner::test_user_wins_scenarios
```

### Test Coverage Goals

- Aim for at least 90% code coverage
- All new features must include tests
- Bug fixes should include regression tests

## Coding Standards

### Python Style Guide

This project follows [PEP 8](https://pep8.org/) style guidelines:

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 79 characters
- Use meaningful variable and function names
- Add docstrings to all functions, classes, and modules
- Use type hints where appropriate (Python 3.7+)

### Code Quality

- Write clear, self-documenting code
- Keep functions small and focused on a single task
- Avoid unnecessary complexity
- Comment complex logic
- Remove commented-out code before committing

### Example Code Style

```python
def determine_winner(user_choice: str, computer_choice: str) -> str:
    """
    Determine the winner of the game based on user and computer choices.
    
    Args:
        user_choice: The user's choice ('rock', 'paper', or 'scissors')
        computer_choice: The computer's choice ('rock', 'paper', or 'scissors')
    
    Returns:
        A string indicating the result: "You win!", "You lose!", or "It's a tie!"
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    # ... rest of implementation
```

## Commit Message Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without functionality changes
- **test**: Adding or updating tests
- **chore**: Changes to build process or auxiliary tools

### Examples

```bash
feat(game): add score tracking functionality

Add ability to track wins, losses, and ties across multiple rounds.
Includes persistent storage of scores.

Closes #42

---

fix(input): improve input validation error messages

Users now receive clearer feedback when entering invalid choices.

---

docs(readme): update installation instructions

Added instructions for development setup and testing.

---

test(winner): add edge case tests for determine_winner

Added tests for all possible win/lose/tie combinations.
```

### Commit Message Rules

- Use the imperative mood ("Add feature" not "Added feature")
- First line should be 50 characters or less
- Provide detailed description in the body if needed
- Reference issues and pull requests when applicable
- Use present tense

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the `question` label
- Reach out to the maintainers
- Check existing issues and pull requests

## Recognition

Contributors will be recognized in the project README and release notes. Thank you for making this project better!

---

**Happy Contributing! 🎮**
