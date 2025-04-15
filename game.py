import sys
import pygame

pygame.init()

pygame.display.set_caption("Ninja Game")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
    #force loop to run at 60 fps
    clock.tick(60)