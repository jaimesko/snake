import sys
import pygame
from typing import Tuple
from constants import Color, Grid, Direction
from entities import Snake, Food

class Game:
    # Constant for game speed
    FPS: int = 5

    def __init__(self) -> None:
        # Initialize pygame
        pygame.init()

        # Create the window
        self.screen: pygame.Surface = pygame.display.set_mode((Grid.WIDTH, Grid.HEIGHT))
        pygame.display.set_caption("Game of Life")

        # Clock
        self.clock: pygame.time.Clock = pygame.time.Clock()

        # Game state
        self.running: bool = True

        # Score
        self.score: int = 0
        self.max_score: int = 0

    def handle_events(self, snake: 'Snake') -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused: bool = True 
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_LEFT:
                    snake.direction = Direction.LEFT.value if snake.direction != Direction.RIGHT.value else snake.direction
                if event.key == pygame.K_RIGHT:
                    snake.direction = Direction.RIGHT.value if snake.direction != Direction.LEFT.value else snake.direction
                if event.key == pygame.K_UP:
                    snake.direction = Direction.UP.value if snake.direction != Direction.DOWN.value else snake.direction
                if event.key == pygame.K_DOWN:
                    snake.direction = Direction.DOWN.value if snake.direction != Direction.UP.value else snake.direction
            if event.type == pygame.KEYUP:
                pass

    def update(self, snake: 'Snake', food: 'Food') -> None:
        # Update game state here

        snake.move()
        # Food collision
        if snake.food_collision(food):
            food.random_spawn(snake)
            self.score += 1
        # Self collision
        if snake.self_collision():
            self.running = False
        # Wall collision
        if snake.wall_collision():
            self.running = False

    # Draw game state here
    def draw(self, snake: 'Snake', food: 'Food', color: Tuple[int, int, int] = Color.GRID_COLOR.value) -> None:
        self.screen.fill(Color.GREEN.value)

        for x in range(0, Grid.WIDTH, Grid.CELL_SIZE):
            pygame.draw.line(self.screen, color, (x, 0), (x, Grid.HEIGHT))
        for y in range(0, Grid.HEIGHT, Grid.CELL_SIZE):
            pygame.draw.line(self.screen, color, (0, y), (Grid.WIDTH, y))

        food.draw(screen=self.screen)
        snake.draw(screen=self.screen)

    def run(self) -> None:
        self.score = 0
        self.start_menu() #self.running #running = self.start_menu()
        snake: 'Snake' = Snake()
        food: 'Food' = Food()
        self.draw(snake, food)
        self.running = True
        # Start the game loop
        while self.running:
            self.handle_events(snake)
            self.update(snake, food)
            self.draw(snake, food)
            pygame.display.flip()
            self.clock.tick(self.FPS)

            # Added by me
            if not self.running:
                self.max_score = max(self.max_score, self.score)
                self.running = self.game_over()
                # Use recursion if there is not an outer while True loop
                if self.running:
                    self.run()
    
    # Start menu
    def start_menu(self) -> bool:
        # Set up the font and text for the menu
        font: pygame.font.Font = pygame.font.SysFont(None, 40)
        title_text: pygame.Surface = font.render("Snake Game", True, Color.WHITE.value)
        start_text: pygame.Surface = font.render("Press SPACE to start", True, Color.WHITE.value) 

        # Calculate the position for the texts
        title_pos: Tuple[int, int] = ((Grid.WIDTH - title_text.get_width()) // 2, Grid.HEIGHT // 3)
        start_pos: Tuple[int, int] = ((Grid.WIDTH - start_text.get_width()) // 2, Grid.HEIGHT // 2)

        # Display the menu on the screen
        self.screen.fill(Color.BLACK.value)
        self.screen.blit(title_text, title_pos)
        self.screen.blit(start_text, start_pos)
        pygame.display.flip()

        # Wait for the user to press SPACE
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return True

    # Game over screen
    def game_over(self) -> bool:
        # Set up the font and text for the menu
        font: pygame.font.Font = pygame.font.SysFont(None, 40)
        title_text: pygame.Surface = font.render("Game Over", True, Color.WHITE.value)
        score_text: pygame.Surface = font.render(f"Score: {self.score}", True, Color.WHITE.value)
        max_score_text: pygame.Surface = font.render(f"Max Score: {self.max_score}", True, Color.WHITE.value)
        start_text: pygame.Surface = font.render("Press SPACE to restart", True, Color.WHITE.value)

        # Calculate the position for the texts
        title_pos: Tuple[int, int] = ((Grid.WIDTH - title_text.get_width()) // 2, Grid.HEIGHT // 4)
        score_pos: Tuple[int, int] = ((Grid.WIDTH - score_text.get_width()) // 2, Grid.HEIGHT // 2 - 50)
        max_score_pos: Tuple[int, int] = ((Grid.WIDTH - max_score_text.get_width()) // 2, Grid.HEIGHT // 2)
        start_pos: Tuple[int, int] = ((Grid.WIDTH - start_text.get_width()) // 2, Grid.HEIGHT // 4 * 3)

        # Display the menu on the screen
        self.screen.fill(Color.BLACK.value)
        self.screen.blit(title_text, title_pos)
        self.screen.blit(score_text, score_pos)
        self.screen.blit(max_score_text, max_score_pos)
        self.screen.blit(start_text, start_pos)
        pygame.display.flip()

        # Wait for the user to press SPACE
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return True # break if not using return