import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Set up the game objects
ball = pygame.Rect(width/2 - 10, height/2 - 10, 20, 20)
paddle1 = pygame.Rect(50, height/2 - 50, 20, 100)
paddle2 = pygame.Rect(width - 70, height/2 - 50, 20, 100)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
paddle_speed = 7

# Set up the game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles based on input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < height:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < height:
        paddle2.y += paddle_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the walls
    if ball.top < 0 or ball.bottom > height:
        ball_speed_y *= -1
    if ball.left < 0 or ball.right > width:
        ball_speed_x *= -1

    # Bounce the ball off the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Draw the game objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (width/2, 0), (width/2, height))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()