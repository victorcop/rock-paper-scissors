"""Tests for the command-line interface."""

import unittest
from unittest.mock import patch
from io import StringIO
import sys

from rock_paper_scissors.__main__ import parse_args, main, setup_logging


class TestParseArgs(unittest.TestCase):
    """Test command-line argument parsing."""

    def test_default_args(self):
        """Test parsing with no arguments (defaults)."""
        args = parse_args([])
        self.assertEqual(args.rounds, 1)
        self.assertFalse(args.verbose)
        self.assertFalse(args.debug)

    def test_rounds_short_option(self):
        """Test parsing rounds with short option."""
        args = parse_args(["-r", "5"])
        self.assertEqual(args.rounds, 5)

    def test_rounds_long_option(self):
        """Test parsing rounds with long option."""
        args = parse_args(["--rounds", "10"])
        self.assertEqual(args.rounds, 10)

    def test_verbose_flag(self):
        """Test parsing verbose flag."""
        args = parse_args(["-v"])
        self.assertTrue(args.verbose)

        args = parse_args(["--verbose"])
        self.assertTrue(args.verbose)

    def test_debug_flag(self):
        """Test parsing debug flag."""
        args = parse_args(["--debug"])
        self.assertTrue(args.debug)

    def test_combined_options(self):
        """Test parsing multiple options together."""
        args = parse_args(["-r", "3", "-v", "--debug"])
        self.assertEqual(args.rounds, 3)
        self.assertTrue(args.verbose)
        self.assertTrue(args.debug)


class TestMain(unittest.TestCase):
    """Test main function."""

    @patch("rock_paper_scissors.__main__.play_multiple_rounds")
    @patch("builtins.input", return_value="rock")
    def test_main_single_round(self, mock_input, mock_play_multiple):
        """Test main with single round (default)."""
        mock_play_multiple.return_value = {"user": 1, "computer": 0, "ties": 0}
        exit_code = main([])
        self.assertEqual(exit_code, 0)
        mock_play_multiple.assert_called_once_with(1, verbose=False)

    @patch("rock_paper_scissors.__main__.play_multiple_rounds")
    @patch("builtins.input", return_value="rock")
    def test_main_multiple_rounds(self, mock_input, mock_play_multiple):
        """Test main with multiple rounds."""
        mock_play_multiple.return_value = {"user": 2, "computer": 1, "ties": 0}
        exit_code = main(["-r", "3"])
        self.assertEqual(exit_code, 0)
        mock_play_multiple.assert_called_once_with(3, verbose=False)

    @patch("sys.stderr", new_callable=StringIO)
    def test_main_invalid_rounds(self, mock_stderr):
        """Test main with invalid rounds value."""
        exit_code = main(["-r", "0"])
        self.assertEqual(exit_code, 1)
        self.assertIn("Error", mock_stderr.getvalue())

    @patch(
        "rock_paper_scissors.__main__.play_multiple_rounds",
        side_effect=KeyboardInterrupt,
    )
    @patch("builtins.input", return_value="rock")
    def test_main_keyboard_interrupt(self, mock_input, mock_play_multiple):
        """Test main handles Ctrl+C gracefully."""
        exit_code = main([])
        self.assertEqual(exit_code, 130)

    @patch(
        "rock_paper_scissors.__main__.play_multiple_rounds",
        side_effect=Exception("Test error"),
    )
    @patch("builtins.input", return_value="rock")
    @patch("sys.stderr", new_callable=StringIO)
    def test_main_unexpected_error(self, mock_stderr, mock_input, mock_play_multiple):
        """Test main handles unexpected errors."""
        exit_code = main([])
        self.assertEqual(exit_code, 1)
        self.assertIn("error", mock_stderr.getvalue().lower())


class TestSetupLogging(unittest.TestCase):
    """Test logging setup."""

    def test_setup_logging_default(self):
        """Test logging setup with default (WARNING) level."""
        setup_logging(verbose=False, debug=False)
        # If no exception is raised, the test passes

    def test_setup_logging_verbose(self):
        """Test logging setup with INFO level."""
        setup_logging(verbose=True, debug=False)
        # If no exception is raised, the test passes

    def test_setup_logging_debug(self):
        """Test logging setup with DEBUG level."""
        setup_logging(verbose=False, debug=True)
        # If no exception is raised, the test passes


if __name__ == "__main__":
    unittest.main()
