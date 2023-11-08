import sys
import pygame
from game import Game
from logging_config import setup_logger

# Configure logging
logger = setup_logger(__name__, 'snake.log')

if __name__ == "__main__":
    try:
        # Initialize and run the game
        game = Game()
        game.run()
    except Exception as e:
        # Error level logging for exceptions
        logger.exception(e) 

        pygame.quit()
        sys.exit()