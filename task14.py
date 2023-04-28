import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the player
player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemies
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []
for i in range(5):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-screen_height, 0)
    enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemies.append(enemy)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += player_speed

    # Move the enemies
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > screen_height:
            enemy.x = random.randint(0, screen_width - enemy_width)
            enemy.y = random.randint(-screen_height, 0)

    # Check for collisions
    for enemy in enemies:
        if player.colliderect(enemy):
            pygame.quit()
            quit()

    # Draw the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.display.update()

    # Set the game's FPS
    clock.tick(60)
