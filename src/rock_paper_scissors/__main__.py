"""Command-line interface for Rock Paper Scissors game."""

import argparse
import logging
import sys
from typing import Optional

from rock_paper_scissors.rock_paper_scissors import play_game, play_multiple_rounds


def setup_logging(verbose: bool, debug: bool) -> None:
    """
    Configure logging based on verbosity level.
    
    Args:
        verbose: Enable INFO level logging.
        debug: Enable DEBUG level logging.
    """
    if debug:
        level = logging.DEBUG
    elif verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def parse_args(args: Optional[list] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Args:
        args: List of arguments to parse (for testing). If None, uses sys.argv.
    
    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog='rock-paper-scissors',
        description='Play Rock, Paper, Scissors game against the computer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rock-paper-scissors                    # Play one round
  rock-paper-scissors -r 5               # Play 5 rounds
  rock-paper-scissors --rounds 3 -v      # Play 3 rounds with verbose output
  rock-paper-scissors --debug            # Enable debug logging
        """
    )
    
    parser.add_argument(
        '-r', '--rounds',
        type=int,
        default=1,
        metavar='N',
        help='number of rounds to play (default: 1)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='enable verbose output (shows more game details)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='enable debug logging (shows all logging messages)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    return parser.parse_args(args)


def main(args: Optional[list] = None) -> int:
    """
    Main entry point for the game.
    
    Args:
        args: List of arguments to parse (for testing). If None, uses sys.argv.
    
    Returns:
        int: Exit code (0 for success, non-zero for error).
    """
    parsed_args = parse_args(args)
    
    # Setup logging
    setup_logging(parsed_args.verbose, parsed_args.debug)
    logger = logging.getLogger(__name__)
    
    # Validate rounds
    if parsed_args.rounds < 1:
        print("Error: Number of rounds must be at least 1", file=sys.stderr)
        logger.error(f"Invalid rounds value: {parsed_args.rounds}")
        return 1
    
    try:
        # Play the game (always use multiple rounds approach for consistent feedback)
        logger.info(f"Starting game with {parsed_args.rounds} round{'s' if parsed_args.rounds > 1 else ''}")
        play_multiple_rounds(parsed_args.rounds, verbose=parsed_args.verbose)
        
        return 0
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
        logger.info("Game interrupted by user (Ctrl+C)")
        return 130
    
    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        logger.exception("Unexpected error occurred")
        return 1


if __name__ == "__main__":
    sys.exit(main())