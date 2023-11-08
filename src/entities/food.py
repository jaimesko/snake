"""
This module defines the Food class, which represents the food in the game.

The Food class includes methods for initializing the food and randomly 
placing the food on the game grid.
"""
import random
import pygame


from constants import Color, Grid

# Imports for type hints
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from .snake import Snake


class Food:
    def __init__(self) -> None:
        self.x: int = Grid.X_CELLS // 4 * 3 * Grid.CELL_SIZE
        self.y: int = Grid.Y_CELLS // 2 * Grid.CELL_SIZE
        self.color: Tuple[int, int, int] = Color.RED.value

    def random_spawn(self, snake: "Snake") -> None:
        self.x = random.randrange(0, Grid.WIDTH, Grid.CELL_SIZE)
        self.y = random.randrange(0, Grid.HEIGHT, Grid.CELL_SIZE)
        # Check if food spawns on snake
        for element in snake.elements:
            if self.x == element[0] and self.y == element[1]:
                self.random_spawn(snake)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen, self.color, (self.x, self.y, Grid.CELL_SIZE, Grid.CELL_SIZE)
        )
