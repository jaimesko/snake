"""events.py"""

import sys
import pygame
from constants import Color, Grid, Direction, GameState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.snake import Snake

class GameEvents:
    @staticmethod
    def handle_events(snake: "Snake") -> None:
        # Handle game events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused: bool = True
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_LEFT:
                    snake.direction = (
                        Direction.LEFT.value
                        if snake.direction != Direction.RIGHT.value
                        else snake.direction
                    )
                if event.key == pygame.K_RIGHT:
                    snake.direction = (
                        Direction.RIGHT.value
                        if snake.direction != Direction.LEFT.value
                        else snake.direction
                    )
                if event.key == pygame.K_UP:
                    snake.direction = (
                        Direction.UP.value
                        if snake.direction != Direction.DOWN.value
                        else snake.direction
                    )
                if event.key == pygame.K_DOWN:
                    snake.direction = (
                        Direction.DOWN.value
                        if snake.direction != Direction.UP.value
                        else snake.direction
                    )
            if event.type == pygame.KEYUP:
                pass

class MenuEvents:
    @staticmethod
    def handle_events():
        # Handle menu events here
        # Start the menu loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.QUIT
                    #pygame.quit()
                    #sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return GameState.GAME

class EndScreenEvents:
    @staticmethod
    def handle_events():
        # Handle end screen events here
        # Start the end screen loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.QUIT
                    #pygame.quit()
                    #sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return GameState.MENU