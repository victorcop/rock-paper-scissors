import unittest
from unittest.mock import patch, call
from rock_paper_scissors.rock_paper_scissors import (
    get_computer_choice,
    get_user_choice,
    determine_winner,
    play_game,
    play_multiple_rounds,
    VALID_CHOICES,
    WIN_CONDITIONS,
)


class TestGetComputerChoice(unittest.TestCase):
    """Test the get_computer_choice function."""
    
    def test_returns_valid_choice(self):
        """Test that computer choice is always one of the valid options."""
        valid_choices = ['rock', 'paper', 'scissors']
        for _ in range(100):  # Test multiple times due to randomness
            choice = get_computer_choice()
            self.assertIn(choice, valid_choices)
    
    def test_randomness(self):
        """Test that computer choice varies (not always the same)."""
        choices = set()
        for _ in range(50):
            choices.add(get_computer_choice())
        # With 50 iterations, we should get at least 2 different choices
        self.assertGreater(len(choices), 1)


class TestGetUserChoice(unittest.TestCase):
    """Test the get_user_choice function."""
    
    @patch('builtins.input', return_value='rock')
    def test_valid_input_rock(self, mock_input):
        """Test that valid input 'rock' is accepted."""
        result = get_user_choice()
        self.assertEqual(result, 'rock')
        mock_input.assert_called_once()
    
    @patch('builtins.input', return_value='paper')
    def test_valid_input_paper(self, mock_input):
        """Test that valid input 'paper' is accepted."""
        result = get_user_choice()
        self.assertEqual(result, 'paper')
    
    @patch('builtins.input', return_value='scissors')
    def test_valid_input_scissors(self, mock_input):
        """Test that valid input 'scissors' is accepted."""
        result = get_user_choice()
        self.assertEqual(result, 'scissors')
    
    @patch('builtins.input', side_effect=['invalid', '  ROCK  '])
    @patch('builtins.print')
    def test_invalid_input_retry(self, mock_print, mock_input):
        """Test that invalid input prompts for retry, and handles case-insensitive input."""
        result = get_user_choice()
        self.assertEqual(result, 'rock')  # ROCK should be normalized to 'rock'
        self.assertEqual(mock_input.call_count, 2)
        # Should print error message for invalid input
        self.assertGreater(mock_print.call_count, 0)
    
    @patch('builtins.input', return_value='  Paper  ')
    def test_input_normalization(self, mock_input):
        """Test that input is normalized (trimmed and lowercased)."""
        result = get_user_choice()
        self.assertEqual(result, 'paper')


class TestDetermineWinner(unittest.TestCase):
    """Test the determine_winner function."""
    
    def test_tie_scenarios(self):
        """Test all tie scenarios."""
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")
        self.assertEqual(determine_winner('paper', 'paper'), "It's a tie!")
        self.assertEqual(determine_winner('scissors', 'scissors'), "It's a tie!")
    
    def test_user_wins_scenarios(self):
        """Test all scenarios where user wins."""
        self.assertEqual(determine_winner('rock', 'scissors'), "You win!")
        self.assertEqual(determine_winner('paper', 'rock'), "You win!")
        self.assertEqual(determine_winner('scissors', 'paper'), "You win!")
    
    def test_user_loses_scenarios(self):
        """Test all scenarios where user loses."""
        self.assertEqual(determine_winner('rock', 'paper'), "You lose!")
        self.assertEqual(determine_winner('paper', 'scissors'), "You lose!")
        self.assertEqual(determine_winner('scissors', 'rock'), "You lose!")


class TestPlayGame(unittest.TestCase):
    """Test the play_game function (integration test)."""
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='rock')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='scissors')
    @patch('builtins.print')
    def test_play_game_user_wins(self, mock_print, mock_computer, mock_user):
        """Test a complete game where user wins."""
        play_game()
        
        # Verify functions were called
        mock_user.assert_called_once()
        mock_computer.assert_called_once()
        
        # Verify output
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any('scissors' in str(call).lower() for call in calls))
        self.assertTrue(any('win' in str(call).lower() for call in calls))
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='paper')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='paper')
    @patch('builtins.print')
    def test_play_game_tie(self, mock_print, mock_computer, mock_user):
        """Test a complete game that results in a tie."""
        play_game()
        
        # Verify output contains tie message
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any('tie' in str(call).lower() for call in calls))
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='scissors')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='rock')
    @patch('builtins.print')
    def test_play_game_user_loses(self, mock_print, mock_computer, mock_user):
        """Test a complete game where user loses."""
        play_game()
        
        # Verify output contains lose message
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any('lose' in str(call).lower() for call in calls))
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='rock')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='scissors')
    @patch('builtins.print')
    def test_play_game_returns_tuple(self, mock_print, mock_computer, mock_user):
        """Test that play_game returns expected tuple."""
        user_choice, computer_choice, result = play_game()
        
        self.assertEqual(user_choice, 'rock')
        self.assertEqual(computer_choice, 'scissors')
        self.assertEqual(result, "You win!")


class TestPlayMultipleRounds(unittest.TestCase):
    """Test the play_multiple_rounds function."""
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='rock')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='scissors')
    @patch('builtins.print')
    def test_multiple_rounds_score_tracking(self, mock_print, mock_computer, mock_user):
        """Test that multiple rounds correctly tracks score."""
        score = play_multiple_rounds(3)
        
        # All rounds should be user wins (rock beats scissors)
        self.assertEqual(score['user'], 3)
        self.assertEqual(score['computer'], 0)
        self.assertEqual(score['ties'], 0)
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='paper')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='paper')
    @patch('builtins.print')
    def test_multiple_rounds_ties(self, mock_print, mock_computer, mock_user):
        """Test that ties are correctly tracked."""
        score = play_multiple_rounds(5)
        
        # All rounds should be ties
        self.assertEqual(score['user'], 0)
        self.assertEqual(score['computer'], 0)
        self.assertEqual(score['ties'], 5)
    
    @patch('rock_paper_scissors.rock_paper_scissors.get_user_choice', return_value='scissors')
    @patch('rock_paper_scissors.rock_paper_scissors.get_computer_choice', return_value='rock')
    @patch('builtins.print')
    def test_multiple_rounds_computer_wins(self, mock_print, mock_computer, mock_user):
        """Test that computer wins are correctly tracked."""
        score = play_multiple_rounds(2)
        
        # All rounds should be computer wins (rock beats scissors)
        self.assertEqual(score['user'], 0)
        self.assertEqual(score['computer'], 2)
        self.assertEqual(score['ties'], 0)


class TestConfiguration(unittest.TestCase):
    """Test configuration constants."""
    
    def test_valid_choices(self):
        """Test that VALID_CHOICES contains expected values."""
        self.assertEqual(VALID_CHOICES, ['rock', 'paper', 'scissors'])
    
    def test_win_conditions(self):
        """Test that WIN_CONDITIONS are correctly defined."""
        self.assertEqual(WIN_CONDITIONS['rock'], 'scissors')
        self.assertEqual(WIN_CONDITIONS['paper'], 'rock')
        self.assertEqual(WIN_CONDITIONS['scissors'], 'paper')


if __name__ == '__main__':
    unittest.main()
