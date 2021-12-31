import pygame

class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1
        
    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)