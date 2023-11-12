"""
This module defines the Game class, which represents the game itself.

The Game class includes methods for initializing the game, running the game loop, 
drawing the game elements on the screen, and handling user input.
"""
import sys
import pygame
from constants import GameState
from entities import Snake, Food
from game_render import GameRender
from events import GameEvents, MenuEvents, EndScreenEvents

class Game:
    # Constant for game speed
    FPS: int = 5

    def __init__(self) -> None:
        self._state = GameState.MENU
        self.score = 0
        self._max_score = 0

        # Initialize game entities
        self.initialize_entities()

        # Initialize pygame
        pygame.init()
        # Create the window
        self.render = GameRender()
        # Clock
        self.clock: pygame.time.Clock = pygame.time.Clock()
    
    def initialize_entities(self) -> None:
        self.snake: "Snake" = Snake()
        self.food: "Food" = Food()

    @property
    def state(self) -> GameState:
        return self._state
    
    @state.setter
    def state(self, state: GameState) -> None:
        if self._state == GameState.MENU and state == GameState.GAME:
            self.initialize()
        elif state == GameState.QUIT:
            pygame.quit()
            sys.exit()
        self._state = state

    @property
    def max_score(self) -> int:
        return self._max_score
    
    @max_score.setter
    def max_score(self, score: int) -> None:
        if score > self._max_score:
            self._max_score = score
            #self.save_max_score()

    def save_max_score(self) -> None:
        with open("max_score.txt", "w") as f:
            f.write(str(self.max_score))

    # Update game state here
    def update(self, snake: "Snake", food: "Food") -> None:
        snake.move()
        # Check for collisions
        if snake.food_collision(food):
            food.random_spawn(snake)
            self.score += 1
        elif snake.self_collision():
            self.state = GameState.END
        elif snake.wall_collision():
            self.state = GameState.END

    def initialize(self) -> None:
        self.score = 0
        self.initialize_entities()
        self.render.draw(self.snake, self.food)

    def run(self) -> None:
        while True:
            if self.state == GameState.MENU:
                self.menu()
            elif self.state == GameState.GAME:
                self.play()
            elif self.state == GameState.END:
                self.end_screen()
            # Limit the game speed
            self.clock.tick(self.FPS)

    def play(self) -> None:
        GameEvents.handle_events(self.snake)
        self.update(self.snake, self.food)
        self.render.draw(self.snake, self.food)

    def menu(self) -> None:
        self.render.start_menu()
        self.state = MenuEvents.handle_events()

    def end_screen(self) -> None:
        self.max_score = self.score
        self.render.end_screen(self.score, self.max_score)
        self.state = EndScreenEvents.handle_events()