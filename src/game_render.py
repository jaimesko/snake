"""Module-level docstring for game_render.py."""

import sys
import pygame
from constants import Color, Grid

# Imports for type hints
from typing import TYPE_CHECKING, List, Tuple
if TYPE_CHECKING:
    from entities.food import Food
    from entities.snake import Snake

class GameRender:

    def __init__(self) -> None:

        # Create the window
        self.screen: pygame.Surface = pygame.display.set_mode((Grid.WIDTH, Grid.HEIGHT))
        pygame.display.set_caption("Game of Life")

    def draw(self, snake: "Snake", food: "Food") -> None:
        # Draw game state here
        self.draw_grid()
        self.draw_snake(snake)
        self.draw_food(food)
        pygame.display.flip()

    def draw_grid(self) -> None:
        
        # Fill the screen with the background color
        self.screen.fill(Color.GREEN.value)

        # Draw the grid lines
        for x in range(0, Grid.WIDTH, Grid.CELL_SIZE):
            pygame.draw.line(self.screen, Color.GRID_COLOR.value, (x, 0), (x, Grid.HEIGHT))
        for y in range(0, Grid.HEIGHT, Grid.CELL_SIZE):
            pygame.draw.line(self.screen, Color.GRID_COLOR.value, (0, y), (Grid.WIDTH, y))
    
    def draw_snake(self, snake: "Snake") -> None:
        for element in snake.elements:
            pygame.draw.rect(
                self.screen,
                snake.color,
                (element[0], element[1], Grid.CELL_SIZE, Grid.CELL_SIZE),
            )

    def draw_food(self, food: "Food") -> None:
        pygame.draw.rect(
            self.screen, food.color, (food.x, food.y, Grid.CELL_SIZE, Grid.CELL_SIZE)
        )

    # Start menu
    def start_menu(self) -> bool:
        # Set up the font and text for the menu
        font: pygame.font.Font = pygame.font.SysFont("Arial", 30)
        title_text: pygame.Surface = font.render("Snake Game", True, Color.WHITE.value)
        start_text: pygame.Surface = font.render(
            "Press SPACE to start", True, Color.WHITE.value
        )

        # Calculate the position for the texts
        title_pos: Tuple[int, int] = (
            (Grid.WIDTH - title_text.get_width()) // 2,
            Grid.HEIGHT // 3,
        )
        start_pos: Tuple[int, int] = (
            (Grid.WIDTH - start_text.get_width()) // 2,
            Grid.HEIGHT // 2,
        )

        # Display the menu on the screen
        self.screen.fill(Color.BLACK.value)
        self.screen.blit(title_text, title_pos)
        self.screen.blit(start_text, start_pos)
        pygame.display.flip()

    # Game over screen
    def end_screen(self, score, max_score) -> bool:
        # Set up the font and text for the menu
        font: pygame.font.Font = pygame.font.SysFont("Arial", 30)
        title_text: pygame.Surface = font.render("Game Over", True, Color.WHITE.value)
        score_text: pygame.Surface = font.render(
            f"Score: {score}", True, Color.WHITE.value
        )
        max_score_text: pygame.Surface = font.render(
            f"Max Score: {max_score}", True, Color.WHITE.value
        )
        start_text: pygame.Surface = font.render(
            "Press SPACE to restart", True, Color.WHITE.value
        )

        # Calculate the position for the texts
        title_pos: Tuple[int, int] = (
            (Grid.WIDTH - title_text.get_width()) // 2,
            Grid.HEIGHT // 4,
        )
        score_pos: Tuple[int, int] = (
            (Grid.WIDTH - score_text.get_width()) // 2,
            Grid.HEIGHT // 2 - 50,
        )
        max_score_pos: Tuple[int, int] = (
            (Grid.WIDTH - max_score_text.get_width()) // 2,
            Grid.HEIGHT // 2,
        )
        start_pos: Tuple[int, int] = (
            (Grid.WIDTH - start_text.get_width()) // 2,
            Grid.HEIGHT // 4 * 3,
        )

        # Display the menu on the screen
        self.screen.fill(Color.BLACK.value)
        self.screen.blit(title_text, title_pos)
        self.screen.blit(score_text, score_pos)
        self.screen.blit(max_score_text, max_score_pos)
        self.screen.blit(start_text, start_pos)
        pygame.display.flip()