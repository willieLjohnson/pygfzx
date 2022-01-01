import pygame
import random
import math

from particle import Particle
from config import *

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fizx')

number_of_particles = 5
particles = []
selected_particle = None
for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    
    particle = Particle(x, y, size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 2)
    
    particles.append(particle)


    
def find_particle(particles, x, y):
    for particle in particles:
        if math.hypot(particle.x - x, particle.y - y) <= particle.size:
            return particle
    return None

global running
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            selected_particle = find_particle(particles, mouse_x, mouse_y)
            if selected_particle:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                selected_particle.x = mouse_x
                selected_particle.y = mouse_y
                selected_particle.color = (255, 0, 0)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    screen.fill(background_color)

    for particle in particles:
        if particle != selected_particle:
            particle.move()
            particle.bounce()
        particle.display(screen)        

    if selected_particle:
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        selected_particle.x = mouse_x
        selected_particle.y = mouse_y
        selected_particle.color = (255, 0, 0)
        
    pygame.display.flip()
