import pygame
import random

from particle import Particle

background_color = (255, 255, 255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fizx')
screen.fill(background_color)


number_of_particles = 10
particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    particles.append(Particle(x, y, size))

    
pygame.display.flip()

global running
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for particle in particles:
        particle.move()
        particle.display(screen)

    pygame.display.flip()
