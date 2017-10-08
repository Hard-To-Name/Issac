import pygame
import player
from random import uniform
from math import sqrt

class hunter():
    def __init__(self, x_index, y_index):
        self.img = pygame.image.load("img/wugu.png").convert_alpha()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x_index, self.y_index = self.generate_pos(x_index, y_index)
        self.speed = 0.3
        self.health = 30
    
    def generate_pos(self, x, y):
        return [uniform(0, x-self.width), uniform(0, y-self.height)]
    
    def get_distance(self, other):
        pos = [other.x_index - self.x_index, other.y_index - self.y_index]
        return sqrt(pos[0]**2 + pos[1]**2)
    
    def move(self, player):
        pos = [player.x_index - self.x_index, player.y_index - self.y_index]
        dis = self.get_distance(player)
        self.x_index += self.speed * (pos[0]/dis)
        self.y_index += self.speed * (pos[1]/dis)