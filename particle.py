import pygame
import math

from config import *
from vector import add_vectors

NORMAL_COLOR = (0, 0, 255) 
ACTIVE_COLOR = (255, 0, 0)  

class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = NORMAL_COLOR
        self.thickness = 1
        self.speed = 0
        self.angle = 0
        
    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)
    
    def move(self):
        (self.angle, self.speed) = add_vectors(self.angle, self.speed, gravity[0], gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = -self.angle
            self.speed *= elasticity


        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

    def activate(self):
        self.color = ACTIVE_COLOR
    
    def deactivate(self):
        self.color = NORMAL_COLOR