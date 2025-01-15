import pygame

# Initialize Pygame
pygame.init()

# Set up display
window = pygame.display.set_mode((500, 500))

# Define colors
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the font
font = pygame.font.Font(None, 74)

# Render the text with a transparent background
text = font.render('GeeksForGeeks', True, green)
text.set_colorkey(blue)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(blue)
    window.blit(text, (100, 200))
    pygame.display.flip()

pygame.quit()
