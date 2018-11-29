from pygame.sprite import Sprite
import pygame
class Arrow(Sprite):
    def __init__(self,theHero):
        super(Arrow,self).__init__()
        self.x = theHero.x
        self.y = theHero.y
        self.speed = 10
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.centerx = self.x
        self.rect.top = self.y
        
        self.arrows = []
        self.arrows.append(pygame.image.load('arrow1.png'))
        self.arrows.append(pygame.image.load('arrow2.png'))
        self.arrows.append(pygame.image.load('arrow3.png'))
        self.arrows.append(pygame.image.load('arrow4.png'))
        self.img = self.arrows[0]
        self.cur_arrow = 0


    def update_me(self):
        self.cur_arrow += 1
        if self.cur_arrow == 4:
            self.cur_arrow = 0
        self.img = self.arrows[self.cur_arrow]       
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        
        
        if self.x > 512:
            self.kill()
