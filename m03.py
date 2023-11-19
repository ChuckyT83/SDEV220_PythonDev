import pygame
from player import Player
pygame.init()

#Setup screen

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
dt = 0

running = True

p1 = Player(50,50,"white")

#main loop for app

while running:
    for event in pygame.event.get():
        #if close button pressed
        if event.type == pygame.QUIT:
            running = False


    screen.fill("green")
    pygame.draw.rect(screen, p1.color,(p1.x, p1.y,10,10))
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.y = p1.y - 1
    if keys[pygame.K_s]:
        p1.y = p1.y + 1
    if keys[pygame.K_a]:
        p1.x = p1.x - 1
    if keys[pygame.K_d]:
        p1.x = p1.x + 1

    dt = clock.tick(60)/1000
    

pygame.quit()