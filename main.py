#ctrl + i
import sys
import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
GRID_COLOR = (75, 225, 75)

# Constants
FPS = 5
CELL_SIZE = 20

X_CELLS = 17
Y_CELLS = 15

WIDTH = X_CELLS * CELL_SIZE
HEIGHT = Y_CELLS * CELL_SIZE

X_MIN = 0
X_MAX = WIDTH - CELL_SIZE
Y_MIN = 0
Y_MAX = HEIGHT - CELL_SIZE

# Directions
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)

# Initialize pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Clock
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.score = 0
        self.size = 3
        self.color = BLUE
        self.direction = RIGHT
        self.elements = [[X_CELLS // 3 * CELL_SIZE, Y_CELLS // 2 * CELL_SIZE],
                         [(X_CELLS // 3 - 1) * CELL_SIZE, Y_CELLS // 2 * CELL_SIZE],
                         [(X_CELLS // 3 - 2) * CELL_SIZE, Y_CELLS // 2 * CELL_SIZE]]

    def grow(self):
        self.size += 1
        self.score += 1

    def move(self):
        head = self.elements[0].copy()

        head[0] += self.direction[0]
        head[1] += self.direction[1]

        self.elements.insert(0, head)
        self.elements = self.elements[:self.size]

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, self.color, (element[0], element[1], CELL_SIZE, CELL_SIZE))

    def self_collision(self):
        if self.elements[0] in self.elements[1:]:
            return True
        else:
            return False
        #for element in self.elements[1:]:
        #    if self.elements[0] == element:
        #        return True
        #return False

    def wall_collision(self):
        if self.elements[0][0] < 0 or self.elements[0][0] > WIDTH - CELL_SIZE:
            return True
        elif self.elements[0][1] < 0 or self.elements[0][1] > HEIGHT - CELL_SIZE:
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
        self.x = X_CELLS // 4 * 3 * CELL_SIZE
        self.y = Y_CELLS // 2 * CELL_SIZE
        self.color = RED

    def random_spawn(self, snake):
        self.x = random.randrange(0, WIDTH, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT, CELL_SIZE)
        # Check if food spawns on snake
        for element in snake.elements:
            if self.x == element[0] and self.y == element[1]:
                self.random_spawn(snake)
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))

def draw_grid(color=GRID_COLOR):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

def draw():
    screen.fill(GREEN)
    draw_grid()


def start_menu():
    # Set up the font and text for the menu
    font = pygame.font.SysFont(None, 20)
    title_text = font.render("Snake Game", True, WHITE)
    start_text = font.render("Press SPACE to start", True, WHITE)

    # Display the menu on the screen
    screen.fill(BLACK)
    screen.blit(title_text, (X_CELLS // 3 * CELL_SIZE, Y_CELLS // 3 * CELL_SIZE))
    screen.blit(start_text, (X_CELLS // 3 * CELL_SIZE, Y_CELLS // 2 * CELL_SIZE))
    pygame.display.flip()

    # Wait for the user to press SPACE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True
            if event.type == pygame.QUIT:
                return False
            
def game_over(snake):
    # Set up the font and text for the menu
    font = pygame.font.SysFont(None, 20)
    title_text = font.render("Game Over", True, WHITE)
    score_text = font.render("Score: " + str(snake.score), True, WHITE)
    start_text = font.render("Press SPACE to restart", True, WHITE)

    # Display the menu on the screen
    screen.fill(BLACK)
    screen.blit(title_text, (X_CELLS // 3 * CELL_SIZE, Y_CELLS // 3 * CELL_SIZE))
    screen.blit(start_text, (X_CELLS // 3 * CELL_SIZE, Y_CELLS // 2 * CELL_SIZE))
    pygame.display.flip()

    # Wait for the user to press SPACE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True
            if event.type == pygame.QUIT:
                return False
        

def main():
    running = start_menu()

    snake = Snake()
    food = Food()

    while running:
        
        screen.fill(GREEN)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True 
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_LEFT:
                    snake.direction = LEFT if snake.direction != RIGHT else snake.direction
                if event.key == pygame.K_RIGHT:
                    snake.direction = RIGHT if snake.direction != LEFT else snake.direction
                if event.key == pygame.K_UP:
                    snake.direction = UP if snake.direction != DOWN else snake.direction
                if event.key == pygame.K_DOWN:
                    snake.direction = DOWN if snake.direction != UP else snake.direction
            if event.type == pygame.KEYUP:
                pass

        #screen.fill(GREEN)
        #draw_grid()
        #food.draw()
        snake.move()
        #snake.draw()


        # Food collision
        if snake.food_collision(food):
            food.random_spawn(snake)

        # Self collision
        if snake.self_collision():
            main()

        # Wall collision
        if snake.wall_collision():
            main()

        food.draw()
        snake.draw()

        pygame.display.flip()
        clock.tick(FPS)

    if running == False:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()


