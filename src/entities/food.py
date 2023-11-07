import random
import pygame

from constants import Color, Grid, Direction


class Food:
    def __init__(self):
        self.x = Grid.X_CELLS // 4 * 3 * Grid.CELL_SIZE
        self.y = Grid.Y_CELLS // 2 * Grid.CELL_SIZE
        self.color = Color.RED.value

    def random_spawn(self, snake):
        self.x = random.randrange(0, Grid.WIDTH, Grid.CELL_SIZE)
        self.y = random.randrange(0, Grid.HEIGHT, Grid.CELL_SIZE)
        # Check if food spawns on snake
        for element in snake.elements:
            if self.x == element[0] and self.y == element[1]:
                self.random_spawn(snake)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, Grid.CELL_SIZE, Grid.CELL_SIZE))