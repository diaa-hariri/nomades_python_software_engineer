import pygame
import random

# Initialize Pygame
pygame.init()

# CONSTANTS
# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

BLOCK_SIZE = 10

# Set up the display
WIDTH, HEIGHT = 640, 480

# init screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set caption
pygame.display.set_caption("Snake Game")

# Point class
class Point(object):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x, self.y = (x, y)

    def copy(self):
        return Point(self.width, self.height, self.x, self.y)
  
    @staticmethod
    def get_random_point(width, height):
        x = random.randint(0, (width-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (height-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        return Point(width, height, x, y)
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

# Food class
class Food:
    position: Point = None

    def __init__(self, snake) -> None:
        self.create_new_food_item(snake)

    def choose_position(self, snake) -> Point:
        p = Point.get_random_point(WIDTH, HEIGHT)
        while p in snake.body:
            p = Point.get_random_point(WIDTH, HEIGHT)
        return p
    
    def create_new_food_item(self, snake) -> None:
        self.position = self.choose_position(snake)

    def draw(self) -> None:
        pygame.draw.rect(screen, RED, (self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE))

# Snake class
class Snake:
    _current_direction: str = ""
    body: list[Point] = []

    def __init__(self) -> None:
        head = Point.get_random_point(WIDTH, HEIGHT)
        self.body = [
            head,
            Point(WIDTH, HEIGHT, head.x - BLOCK_SIZE, head.y),
            Point(WIDTH, HEIGHT, head.x - 2 * BLOCK_SIZE, head.y)
        ]
        self._current_direction = random.choice(["UP", "DOWN", "RIGHT"])
    
    def move(self) -> None:
        head_copy = self.body[0].copy()

        if self._current_direction == "UP":
            head_copy.y -= BLOCK_SIZE
        elif self._current_direction == "DOWN":
            head_copy.y += BLOCK_SIZE
        elif self._current_direction == "LEFT":
            head_copy.x -= BLOCK_SIZE
        elif self._current_direction == "RIGHT":
            head_copy.x += BLOCK_SIZE
        
        self.body = [head_copy] + self.body[:-1]
    
    def change_direction(self, direction: str) -> None:
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if direction != opposite_directions.get(self._current_direction):
            self._current_direction = direction
    
    def grow(self) -> None:
        self.body.append(self.body[-1].copy())

    def check_border_collision(self) -> bool:
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH or head.y < 0 or head.y >= HEIGHT

    def check_self_collision(self) -> bool:
        head = self.body[0]
        return head in self.body[1:]
    
    def check_collision(self, item: Food) -> bool:
        return self.body[0] == item.position
    
    def check_game_over(self) -> bool:
        return self.check_border_collision() or self.check_self_collision()
    
    def draw(self) -> None:
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE))

# Create instances of Snake and Food - Global variables
snake = Snake()
food = Food(snake)


# Helpers functions
def press_space_to_start(font):
  start_text = font.render("Press SPACE to start the game", True, WHITE, BLACK)
  start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
      
  screen.fill(BLACK)
  screen.blit(start_text, start_text_rect)
  pygame.display.flip()

  clock = pygame.time.Clock()
  while True:
      clock.tick(30)  # 30 FPS
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return False
          elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                  return True

def display_score(font, score):
    score_text = font.render(f"Score: {score}", True, WHITE, None)
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, 20))
    screen.blit(score_text, score_text_rect)

# Main function
def snake_game():
  # Game loop
  update_direction: bool = True
  clock = pygame.time.Clock()
  font = pygame.font.Font('freesansbold.ttf', 32)
  score: int = 0

  running: bool = press_space_to_start(font) # -> blocking function

  while running:
      clock.tick(20) # 20 FPS
      
      # ================= EVENT PART =================
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.KEYDOWN and update_direction:
              if event.key == pygame.K_UP:
                  snake.change_direction("UP")
              elif event.key == pygame.K_DOWN:
                  snake.change_direction("DOWN")
              elif event.key == pygame.K_LEFT:
                  snake.change_direction("LEFT")
              elif event.key == pygame.K_RIGHT:
                  snake.change_direction("RIGHT")
              
              update_direction = False
      # ================= END EVENT PART =================

      # ================= LOGIC PART =================
      snake.move()

      if (snake.check_collision(food)):
        snake.grow()
        food.create_new_food_item(snake)
        score += 1

      if(snake.check_game_over()):
          running = False
      # ================= END LOGIC PART =================
      
      # ================= DISPLAY PART =================
      screen.fill(BLACK)
      snake.draw()
      food.draw()
      display_score(font, score)

      pygame.display.update()
      # ================= END DISPLAY PART =================

      update_direction = True

if __name__ == "__main__":
  snake_game()
  pygame.quit()
