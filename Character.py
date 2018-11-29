from pygame.sprite import Sprite
class Character(Sprite):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power
    def is_alive(self):
        myBool = self.health > 0
        return myBool
    def take_damage(self,ammount_of_damage):
        self.health -= ammount_of_damage