import pygame

from constants import Color, Grid, Direction

# Imports for type hints
from typing import TYPE_CHECKING, List, Tuple

if TYPE_CHECKING:
    from .food import Food


class Snake:
    def __init__(self) -> None:
        self.size: int = 3
        self.color: Tuple[int, int, int] = Color.BLUE.value
        self.direction: Tuple[int, int] = Direction.RIGHT.value
        self.elements: List[List[int]] = [
            [Grid.X_CELLS // 3 * Grid.CELL_SIZE, Grid.Y_CELLS // 2 * Grid.CELL_SIZE],
            [
                (Grid.X_CELLS // 3 - 1) * Grid.CELL_SIZE,
                Grid.Y_CELLS // 2 * Grid.CELL_SIZE,
            ],
            [
                (Grid.X_CELLS // 3 - 2) * Grid.CELL_SIZE,
                Grid.Y_CELLS // 2 * Grid.CELL_SIZE,
            ],
        ]

    def move(self) -> None:
        head: List[int] = self.elements[0].copy()

        head[0] += self.direction[0]
        head[1] += self.direction[1]

        self.elements.insert(0, head)
        self.elements = self.elements[: self.size]

    def draw(self, screen: pygame.Surface) -> None:
        for element in self.elements:
            pygame.draw.rect(
                screen,
                self.color,
                (element[0], element[1], Grid.CELL_SIZE, Grid.CELL_SIZE),
            )

    def self_collision(self) -> bool:
        if self.elements[0] in self.elements[1:]:
            return True
        else:
            return False
        # Alternative way to check for self collision
        # for element in self.elements[1:]:
        #    if self.elements[0] == element:
        #        return True
        # return False

    def wall_collision(self) -> bool:
        if self.elements[0][0] < 0 or self.elements[0][0] > Grid.WIDTH - Grid.CELL_SIZE:
            return True
        elif (
            self.elements[0][1] < 0
            or self.elements[0][1] > Grid.HEIGHT - Grid.CELL_SIZE
        ):
            return True
        else:
            return False

    def food_collision(self, food: "Food") -> bool:
        if self.elements[0] == [food.x, food.y]:
            self.grow()
            return True
        else:
            return False

    def grow(self) -> None:
        self.size += 1
