import pygame

from constants import Color, Grid, Direction


class Snake:
    def __init__(self):
        self.size = 3
        self.color = Color.BLUE.value
        self.direction = Direction.RIGHT.value
        self.elements = [[Grid.X_CELLS // 3 * Grid.CELL_SIZE, Grid.Y_CELLS // 2 * Grid.CELL_SIZE],
                         [(Grid.X_CELLS // 3 - 1) * Grid.CELL_SIZE, Grid.Y_CELLS // 2 * Grid.CELL_SIZE],
                         [(Grid.X_CELLS // 3 - 2) * Grid.CELL_SIZE, Grid.Y_CELLS // 2 * Grid.CELL_SIZE]]

    def grow(self):
        self.size += 1

    def move(self):
        head = self.elements[0].copy()

        head[0] += self.direction[0]
        head[1] += self.direction[1]

        self.elements.insert(0, head)
        self.elements = self.elements[:self.size]

    def draw(self, screen):
        for element in self.elements:
            pygame.draw.rect(screen, self.color, (element[0], element[1], Grid.CELL_SIZE, Grid.CELL_SIZE))

    def self_collision(self):
        if self.elements[0] in self.elements[1:]:
            return True
        else:
            return False
        # Alternative way to check for self collision
        #for element in self.elements[1:]:
        #    if self.elements[0] == element:
        #        return True
        #return False

    def wall_collision(self):
        if self.elements[0][0] < 0 or self.elements[0][0] > Grid.WIDTH - Grid.CELL_SIZE:
            return True
        elif self.elements[0][1] < 0 or self.elements[0][1] > Grid.HEIGHT - Grid.CELL_SIZE:
            return True
        else:
            return False
        
    def food_collision(self, food):
        if self.elements[0] == [food.x, food.y]:
            self.grow()
            return True
        else:
            return False