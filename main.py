import pygame
from particle import Particle

background_color = (255, 255, 255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fizx')

particle = Particle(150, 50, 15)

screen.fill(background_color)
particle.display(screen)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

