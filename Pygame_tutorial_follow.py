import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("tictactoe.png")
pygame.display.set_icon(icon)


# Player
PlayerImg = pygame.image.load("cross.png")
PlayerImg = pygame.transform.scale(PlayerImg,(32,32))
PlayerX = 370
PlayerY = 480
Player_change = 0.1
def player(x,y):
    screen.blit(PlayerImg,(x,y))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen color with RGB
    screen.fill((255,255,220))

    # check if left or right arrow is pressed

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            PlayerX -= Player_change
        if event.key == pygame.K_RIGHT:
            PlayerX += Player_change
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            pass
            #print("keypress has been released")

    player(PlayerX,PlayerY)
    pygame.display.update()