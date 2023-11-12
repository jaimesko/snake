"""
This is the main module of the game. It initializes and runs the game, 
and handles any exceptions that occur during the game.

If an exception occurs, it is logged to a file and the game is exited.
"""
import sys
import pygame
from game import Game
from logging_config import setup_logger


def main() -> None:
    try:
        # Initialize and run the game
        game: Game = Game()
        game.run()
    except Exception as e:
        # Configure logger
        logger = setup_logger(__name__, "snake.log")
        # Error level logging for exceptions
        logger.exception(e)

        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
