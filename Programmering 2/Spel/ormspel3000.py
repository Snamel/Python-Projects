import pygame
import random
import os


# Initialize Pygame
pygame.init()

# Play the music on loop
pygame.mixer.init()
background_music_file = "gamingmuskk.mp3"
pygame.mixer.music.load(background_music_file)
pygame.mixer.music.play(-1)

# Set up the game window
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
PINK = (159, 43, 104)

player_color = GREEN
# Set the font for the menu
font_title = pygame.font.SysFont(None, 48)
font_button = pygame.font.SysFont(None, 32)

# Set the clock to control the game's FPS
clock = pygame.time.Clock()

# Initialize the game state
game_state = "menu"


# Define the snake's starting position and size
snake_size = 20
snake_x = 300
snake_y = 300


# Get snake image
player_image_file = "player_image.png"
player_image = pygame.image.load(player_image_file)
player_image = pygame.transform.scale(player_image, (snake_size, snake_size))

# Get fruit image
fruit_image_file = "fruit_image.png"
fruit_image = pygame.image.load(fruit_image_file)
fruit_image = pygame.transform.scale(fruit_image, (snake_size, snake_size))


# Define the initial velocity of the snake
velocity_x = 0
velocity_y = 0

# Define the food's position
food_x = random.randint(0, WIDTH - snake_size) // snake_size * snake_size
food_y = random.randint(0, HEIGHT - snake_size) // snake_size * snake_size

# Initialize the score counter
score = 0

# Initialize the snake's body
snake_body = []
snake_length = 1

movement_multiplier = 1

# Game loop
while True:
    if game_state == "menu":
        # Menu loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "running"

        win.fill(BLACK)
        title_text = font_title.render("Snake Game", True, WHITE)
        start_text = font_button.render("Press ENTER to start", True, GRAY)
        win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height()))
        win.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + title_text.get_height()))

    elif game_state == "running":
        # Game running loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and velocity_y != snake_size:
                    velocity_x = 0
                    velocity_y = -snake_size * movement_multiplier
                elif event.key == pygame.K_s and velocity_y != -snake_size:
                    velocity_x = 0
                    velocity_y = snake_size * movement_multiplier
                elif event.key == pygame.K_a and velocity_x != snake_size:
                    velocity_x = -snake_size * movement_multiplier
                    velocity_y = 0
                elif event.key == pygame.K_d and velocity_x != -snake_size:
                    velocity_x = snake_size * movement_multiplier
                    velocity_y = 0
                elif event.type == pygame.KMOD_SHIFT and score > 20:
                    movement_multiplier = 1.5
                    player_color = PINK
            elif event.type == pygame.KEYUP:
                if event.key == pygame.KMOD_SHIFT:
                    movement_multiplier = 1
                    player_color = GREEN

        # Update the snake's position
        snake_x += velocity_x
        snake_y += velocity_y

        # Check if the snake has collided with the food
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randint(0, WIDTH - snake_size) // snake_size * snake_size
            food_y = random.randint(0, HEIGHT - snake_size) // snake_size * snake_size
            score += 1
            snake_length += 1

        # Check if the snake has collided with the game borders or itself
        if (
            snake_x < 0
            or snake_x >= WIDTH
            or snake_y < 0
            or snake_y >= HEIGHT
            or [snake_x, snake_y] in snake_body[1:]
        ):
            game_state = "game_over"

        # Fill the game window with the background color
        win.fill(BLACK)

        # Update the snake's body
        snake_body.append([snake_x, snake_y])
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Draw the snake
        for body_part in snake_body:
            pygame.draw.rect(win, player_color, (body_part[0], body_part[1], snake_size, snake_size))

        # Draw the food
        pygame.draw.rect(win, RED, (food_x, food_y, snake_size, snake_size))

        # Draw the score counter
        score_text = font_button.render("Score: " + str(score), True, WHITE)
        win.blit(score_text, (10, 10))

    elif game_state == "game_over":
        # Game over loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "running"
                    snake_x = 300
                    snake_y = 300
                    velocity_x = 0
                    velocity_y = 0
                    score = 0
                    food_x = random.randint(0, WIDTH - snake_size) // snake_size * snake_size
                    food_y = random.randint(0, HEIGHT - snake_size) // snake_size * snake_size
                    snake_body = []
                    snake_length = 1
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        win.fill(BLACK)
        game_over_text = font_title.render("Game Over", True, WHITE)
        score_text = font_button.render("Score: " + str(score), True, WHITE)
        restart_text = font_button.render("Press ENTER to restart", True, GRAY)
        quit_text = font_button.render("Press Q to quit", True, GRAY)
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height()))
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        win.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height()))
        win.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height() + restart_text.get_height()))

    # Update the game display
    pygame.display.update()

    # Set the game's FPS
    clock.tick(12)
