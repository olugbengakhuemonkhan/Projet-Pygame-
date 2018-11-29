from math import hypot
from pygame.sprite import Sprite
import pygame
class BadGuy(Sprite):
    def __init__(self):
        super(BadGuy,self).__init__()
        self.x = 200
        self.y = 200
        self.speed = 5
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.img = pygame.image.load('goblin.png')
    def update_me(self, theHero):
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx, dy) 
        if dist == 0:
            dist = 1


        dx = dx/ dist
        dy = dx/ dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.x = self.x
        self.rect.y = self.y
