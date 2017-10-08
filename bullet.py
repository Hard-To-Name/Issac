import pygame
from math import sqrt

class bullet():
    def __init__(self, user, directions):
        # user: player/hunter who shoots it
        self.img = pygame.image.load("img/bullet.png").convert_alpha()
        self.user = user
        self.x_index = user.x_index
        self.y_index = user.y_index
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.directions = directions
        self.speed = 0.5
    
    def move(self):
        # directions format [up, down, left, right], int type
        x = self.directions[3] - self.directions[2]
        y = self.directions[1] - self.directions[0]
        if x != 0 and y != 0:
            self.x_index += x*self.speed/(sqrt(2))
            self.y_index += y*self.speed/(sqrt(2))
        elif x != 0:
            self.x_index += x*self.speed
        elif y != 0:
            self.y_index += y*self.speed
    
    def finish(self, back_x, back_y, goals):
        # determine if the bullet hit the boundary or its goals
        if self.reach_boundary(back_x, back_y): return True
        for g in goals:
            if self.get_distance(g) < 0.5 * (self.width + g.width):
                g.health -= 10
                return True
                break
        return False
    
    def reach_boundary(self, x, y):
        # value format [x, y] of  move()
        if 0 >= self.x_index or self.x_index + self.width >= x: return True
        if 0 >= self.y_index or self.y_index + self.height >= y: return True
        return False
    
    def get_distance(self, other):
        pos = [other.x_index - self.x_index, other.y_index - self.y_index]
        return sqrt(pos[0]**2 + pos[1]**2)