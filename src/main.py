import sys
import logging
import pygame
from game import Game

# Configure logging
logging.basicConfig(filename='snake.log', level=logging.ERROR)

if __name__ == "__main__":
    try:
        # Initialize and run the game
        game = Game()
        game.run()
    except Exception as e:
        # Error level logging for exceptions
        logging.exception(e) 
        
        pygame.quit()
        sys.exit()