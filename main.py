import pygame
import random
import math

from particle import Particle
from config import *

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fizx')

number_of_particles = 10
particles = []
for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    
    particle = Particle(x, y, size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)
    
    particles.append(particle)

global running
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for particle in particles:
        particle.move()
        particle.bounce()
        particle.display(screen)

    pygame.display.flip()
