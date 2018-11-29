import pygame.font
import pygame


class Start_Button2(object):
    def __init__(self, screen):
        # print "Start Button"
        # get the screen, and save it to this object
        self.screen = screen
        # how big is the screen? We need a rect
        self.screen_rect = self.screen.get_rect()
        # self.monthsMessage2 = monthsMessage2

        # set the width of the button image
        self.width = 450
        # set the height
        self.height = 50
        # set some colors

        # green = (0,200,150)
        self.button2_color = 0, 0, 0
        self.text_color = 240, 240, 240
        self.text_size = 240, 240, 240
        # get font from pygame
        self.font = pygame.font.Font(None, 16)
        # set the rect of the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # set the location of the rect
        self.rect.center = self.screen_rect.center

    def setup_message(self, user_name ):
        # setup the message!
        self.image_message = self.font.render("THE BRAVE ONE. THE WALKERS DIE AND RETURN STRONGER. KILL THEM !!! ",  True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
        self.user_name = user_name

    def draw_button2(self):
        # fill in the button
        self.screen.fill(self.button2_color, self.rect)
        # actually draw the button
        self.screen.blit(self.image_message, self.image_message_rect)

        # def setup_message(self, user_name, ):
        # # setup the message!
        #     self.image_message = self.font.render("WELCOME! " + user_name + ' ' + self.monthsMessage2,True, self.text_color)
        #     self.image_message_rect = self.image_message.get_rect()
        #     self.image_message_rect.center = self.rect.center
        #     self.user_name = user_name
    
        # def draw_button(self):
        #     # fill in the button
        #     self.screen.fill(self.button_color,self.rect)
        #     # actually draw the button
        #     self.screen.blit(self.image_message,self.image_message_rect)

