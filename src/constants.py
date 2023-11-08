from enum import Enum


# An Enum for Colors
class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (200, 50, 50)
    GREEN = (50, 200, 50)
    BLUE = (50, 50, 200)
    GRID_COLOR = (75, 225, 75)


class Grid:
    # Constant for cell size
    CELL_SIZE = 20
    # Constants for grid dimensions
    X_CELLS = 17
    Y_CELLS = 15
    WIDTH = X_CELLS * CELL_SIZE
    HEIGHT = Y_CELLS * CELL_SIZE
    # Constants for grid boundaries
    X_MIN = 0
    X_MAX = WIDTH - CELL_SIZE
    Y_MIN = 0
    Y_MAX = HEIGHT - CELL_SIZE


# An Enum for Directions
class Direction(Enum):
    LEFT = (-Grid.CELL_SIZE, 0)
    RIGHT = (Grid.CELL_SIZE, 0)
    UP = (0, -Grid.CELL_SIZE)
    DOWN = (0, Grid.CELL_SIZE)
