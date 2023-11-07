#ctrl + i
import sys
import pygame
import random
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

class Game:
    # Constant for game speed
    FPS = 5

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode((Grid.WIDTH, Grid.HEIGHT))
        pygame.display.set_caption("Game of Life")

        # Clock
        self.clock = pygame.time.Clock()

        # Game state
        self.running = True

        # Score
        self.score = 0
        self.max_score = 0

    def handle_events(self, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True 
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

    def update(self, snake, food):
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
    def draw(self, snake, food, color=Color.GRID_COLOR.value):
        self.screen.fill(Color.GREEN.value)

        for x in range(0, Grid.WIDTH, Grid.CELL_SIZE):
            pygame.draw.line(self.screen, color, (x, 0), (x, Grid.HEIGHT))
        for y in range(0, Grid.HEIGHT, Grid.CELL_SIZE):
            pygame.draw.line(self.screen, color, (0, y), (Grid.WIDTH, y))

        food.draw(screen=self.screen)
        snake.draw(screen=self.screen)

    def run(self):
        #while True:
        # Added by me
        self.score = 0
        self.start_menu() #self.running #running = self.start_menu()
        snake = Snake()
        food = Food()
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
    def start_menu(self):
        # Set up the font and text for the menu
        font = pygame.font.SysFont(None, 40)
        title_text = font.render("Snake Game", True, Color.WHITE.value)
        start_text = font.render("Press SPACE to start", True, Color.WHITE.value) 

        # Calculate the position for the texts
        title_pos = ((Grid.WIDTH - title_text.get_width()) // 2, Grid.HEIGHT // 3)
        start_pos = ((Grid.WIDTH - start_text.get_width()) // 2, Grid.HEIGHT // 2)

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
    def game_over(self):
        # Set up the font and text for the menu
        font = pygame.font.SysFont(None, 40)
        title_text = font.render("Game Over", True, Color.WHITE.value)
        score_text = font.render(f"Score: {self.score}", True, Color.WHITE.value)
        max_score_text = font.render(f"Max Score: {self.max_score}", True, Color.WHITE.value)
        start_text = font.render("Press SPACE to restart", True, Color.WHITE.value)

        # Calculate the position for the texts
        title_pos = ((Grid.WIDTH - title_text.get_width()) // 2, Grid.HEIGHT // 4)
        score_pos = ((Grid.WIDTH - score_text.get_width()) // 2, Grid.HEIGHT // 2 - 50)
        max_score_pos = ((Grid.WIDTH - max_score_text.get_width()) // 2, Grid.HEIGHT // 2)
        start_pos = ((Grid.WIDTH - start_text.get_width()) // 2, Grid.HEIGHT // 4 * 3)

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

if __name__ == "__main__":
    # Initialize and run the game
    game = Game()
    game.run()