"""
This package contains the modules for the game entities: Snake and Food.

The Snake module defines the behavior of the snake in the game.
The Food module defines the behavior of the food that the snake eats.
"""

# Define what is available to import from the package when using from <package> import *
__all__ = ['Snake', 'Food']

from .snake import Snake
from .food import Food
