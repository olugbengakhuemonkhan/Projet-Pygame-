from random import randint
# this is a subclass of Character. So go get Character
from Character import Character
# import random
import pygame
from pygame.sprite import Sprite

# class Vampire(object):
from math import hypot
class Adventurer(Sprite):
    def __init__(self):
        # call parent/super init method
        super(Adventurer, self).__init__()
        # randomPower = random.randint(2,5)
        randomPower = randint(4,7)
        self.name = "adventurer"
        self.health = 15
        self.power = randomPower
        self.x = 200
        self.y = 200
        self.speed = 2
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.top = self.y 
        self.img = pygame.image.load('adventurer1.png') 
        self.cur_adventurer = 0      
    def take_damage(self,ammount_of_damage, game):
        self.health += ammount_of_damage
        if self.is_alive():
            game.updateTotal(10)
    def is_alive(self):
        return self.health < 0
        
    def make_girls_swoon(self):
        print "The skin of the Cullens flashes like diamonds."

        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False
    def shouldMove(self,direction, start = True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if(direction == "down"):
            self.should_move_down = start
        if(direction == "up"): 
            self.should_move_up = start
    def draw_me(self):
        if(self.should_move_right):
            if self.x < 480:
                self.x += self.speed
        elif(self.should_move_left):
            if self.x > 32:
                self.x -= self.speed
        if(self.should_move_down):
            if self.y < 420:
                self.y += self.speed
        elif self.should_move_up:
            if self.y > 32:
                self.y -= self.speed
    def update_me(self, theHero):
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy /dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.x = self.x
        self.rect.y = self.y

        self.adventurers = []
        self.adventurers.append(pygame.image.load('adventurer1.png'))
        self.adventurers.append(pygame.image.load('adventurer2.png'))
        self.adventurers.append(pygame.image.load('adventurer3.png'))
        self.adventurers.append(pygame.image.load('adventurer4.png'))
        self.img = self.adventurers[0]
        
        self.cur_adventurer += 1
        if self.cur_adventurer == 4:
            self.cur_adventurer = 0
        self.img = self.adventurers[self.cur_adventurer]       
    #     self.x += self.speed
    #     self.rect.x = self.x
    #     self.rect.y = self.y
        
        
        if self.x > 512:
            self.kill()