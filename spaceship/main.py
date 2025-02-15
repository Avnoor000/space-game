import pygame
import random
import time

pygame.init()
# Colors
black = [0, 0, 0]
white = [255, 255, 255]

# Screen setup
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space shooting')
bg = pygame.image.load('galaxy.jpg')
bg = pygame.transform.scale(bg, (width, height))

# Sprite setup
pos = [300, 550]
player = pygame.image.load('space-ship.png')
player = pygame.transform.scale(player, (70, 50))
speed = 10
player_rect = player.get_rect(topleft=pos)

# Explosion setup
explosion = pygame.image.load('explosion.png')
explosion = pygame.transform.scale(explosion, (70, 70))
explosion_pos = [0, 0]

# Projectile properties
m = pygame.image.load('m.png')
m = pygame.transform.scale(m, (40, 40))
initial_projectile_speed = 5
projectiles = []

# frame rate value
frame = 10
value = 100

# Initialize score
score_value = 0
font = pygame.font.Font(None, 32)
score_text = font.render(f"Score: {score_value}", True, white)

# Function to spawn a new projectile
def spawn_projectile():
    x = random.randint(0, width - 40)
    y = -40
    projectiles.append(pygame.Rect(x, y, 40, 40))

clock = pygame.time.Clock()
run = True
spawn_timer = 0
start_time = time.time()
collision_occurred = False

projectile_speed = initial_projectile_speed

while run:
    clock.tick(60)
    spawn_timer += 1
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Increase projectile speed every 3 seconds
    if time.time() - start_time > 3:
        projectile_speed += 1
        start_time = time.time()

    # Spawn a new projectile every 10 frames
    if spawn_timer > frame:
        spawn_projectile()
        spawn_timer = 0

    # Move projectiles
    for projectile in projectiles:
        projectile.y += projectile_speed

    # Remove projectiles that are off-screen
    projectiles = [p for p in projectiles if p.y < height]

    # Player movement
    if keys[pygame.K_LEFT] and pos[0] > 0:
        pos[0] -= speed
    if keys[pygame.K_RIGHT] and pos[0] < width - player.get_width():
        pos[0] += speed

    player_rect.topleft = pos

    # Check for collisions
    for projectile in projectiles:
        if player_rect.colliderect(projectile):
            explosion_pos = pos.copy()  # Capture the position of the spaceship
            collision_occurred = True
            break

    # Fill the screen with black
    screen.fill(black)
    # Display background
    screen.blit(bg, (0, 0))
    # Display spaceship
    screen.blit(player, player_rect.topleft)
    # Display projectiles
    for projectile in projectiles:
        screen.blit(m, (projectile.x, projectile.y))
    # Display explosion and end game if collision occurred
    if collision_occurred:
        screen.blit(explosion, explosion_pos)
        screen.blit(score_text, (500, 300))
        pygame.display.update()
        pygame.time.delay(1000)  # Delay to show the explosion before quitting
        run = False
    else:
        # Update and display score
        score_value += 1
        score_text = font.render(f"Score: {score_value}", True, white)
        screen.blit(score_text, (10, 10))
        if score_value == value:
            value += 100
            if value >= 1000:
                pass
            else:
                frame -= 0.5
        pygame.display.update()

pygame.quit()
