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
        logger = setup_logger(__name__, 'snake.log')
        # Error level logging for exceptions
        logger.exception(e) 

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()