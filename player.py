import math
import pygame
import bullet

class player():
    def __init__(self, x_index, y_index, img_name):
        self.img = pygame.image.load(img_name).convert_alpha()
        self.x_index = 0.5 * x_index - 0.5 * self.img.get_width()
        self.y_index = 0.5 * y_index - 0.5 * self.img.get_height()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.speed = 0.5
        self.health = 100
        self.in_protect = False
        
    def move(self, back_x, back_y, directions):
        # directions format [up, down, left, right], int type
        x = directions[3] - directions[2]
        y = directions[1] - directions[0]
        x, y = self.check_boundary(back_x, back_y, [x, y])
        if x != 0 and y != 0:
            self.x_index += x*self.speed/(math.sqrt(2))
            self.y_index += y*self.speed/(math.sqrt(2))
        elif x != 0:
            self.x_index += x*self.speed
        elif y != 0:
            self.y_index += y*self.speed
    
    def check_boundary(self, x, y, value):
        # value format [x, y] of  move()
        if value[0] == -1 and 0 >= self.x_index: value[0] = 0
        if value[0] == 1 and self.x_index + self.width >= x: value[0] = 0
        if value[1] == -1 and 0 >= self.y_index: value[1] =  0
        if value[1] == 1 and self.y_index + self.height >= y: value[1] = 0
        return value