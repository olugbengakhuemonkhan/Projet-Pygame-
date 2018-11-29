# 1. Include pygame
# we needed pip to get this for us because Python doesnt ship with it


  
import pygame, pygame.font, pygame.event, pygame.draw, string
from raw import get_key
from raw import ask
from raw import display_box
import pygame
from Hero import Hero
from BadGuy import BadGuy
from Arrow import Arrow
from Button import Start_Button
from Button2 import Start_Button2
from adventurer import Adventurer
from age import whatAge
from age2 import whatAge2
# we want to have pygame "groups"
from pygame.sprite import Group,groupcollide

screen = pygame.display.set_mode((512,480))
 
user_name = ask(screen, 'Warrior,say your name? ')





monthsMessage = whatAge()
print monthsMessage

# monthsMessage2 = whatAge2()
# print monthsMessage2

# 2. Initialize Pygame.
# Why do we need to do this? Because they told us to.

pygame.init()

# 3. Make a screen with a size. The size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# set the title of the window that opens...
pygame.display.set_caption("GAME OF 'NO NAME'")

theHero = Hero()
bad_guy = BadGuy()
adventurer = Adventurer()
# make a bad_guys group
bad_guys = Group()
# add the bad_guy to the bad_guys group
bad_guys.add(bad_guy)
bad_guys.add(Adventurer())
# make a start button
start_button = Start_Button(pygame_screen, monthsMessage)
start_button2 = Start_Button2(pygame_screen)
# make a group for our arrows to live in
# a group is a pygame thing. Its like a list,
# but with cool stuff too
arrows = Group()
adventurers = Group()

# ========VARIABLES FOR OUR GAME==========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
# arrow_
# image = pygame.image.load('arrow.png')
tick = 0
# heroLoc = {
#     'x': 100,
#     'y': 100
# }
direction = 1
# =========MAIN GAME LOOP==========
game_on = True
game_start = False
# the loop will run as long as our bool is true
while game_on:
    tick += 1
    if(tick % 120 == 0):
        bad_guys.add(BadGuy()), 
        
    # we are in the game loop from here on out!
    # 5. Listen for events and quit if the user clicks the x
    # =======EVENT CHECKER=========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                # THE USER CLICKED THE RED DOT!
                # These aren't the droids were looking for. quit.
                game_on = False
        elif event.type == pygame.KEYDOWN:
            # the user pressed a key!!!
            print event.key

            if event.key == 275:
                # the user pressed the right arrow!!! Move our dude right
                # heroLoc['x'] += 10
                # theHero.x += 10
                theHero.shouldMove("right")
            elif event.key == 276:
                # the user pressed left arrow!
                # theHero.x -= 10
                theHero.shouldMove("left")
            if event.key == 273:
                # the user pressed the up arrow!
                theHero.shouldMove("up")
            elif event.key == 274:
                theHero.shouldMove("down")
            elif event.key == 32:
                # user pressed space bar... FIRE!!!!
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)
                # print arrows
        elif event.type == pygame.KEYUP:
            # the user RELEASED a key
            if event.key == 275:
                theHero.shouldMove("right",False)
            elif event.key == 276:
                theHero.shouldMove("left",False)
            if event.key == 273:
                theHero.shouldMove("up",False)
            elif event.key == 274:
                theHero.shouldMove("down",False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print mouse_x,mouse_y;
            if start_button.rect.collidepoint(mouse_x, mouse_y):
                game_start = True
                bg_music = pygame.mixer.Sound('faf.wav')
                bg_music.play()
                game_counter = 0
                
    # ==========DRAW STUFF===========
    # we use blit to draw on the screen. blit = block image transfer
    # blit is a method, that takes 2 arg:
    # 1. What to draw
    # 2. Where to draw it
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    if game_start == True and game_counter >= 500:
        theHero.draw_me()
        for enemey in bad_guys:
            enemey.update_me(theHero)
            pygame_screen.blit(enemey.img,[enemey.x,enemey.y])
        for adventurer in adventurers:
            adventurer.update_me()
        for arrow in arrows:
            arrow.update_me()
            pygame_screen.blit(adventurer.img,[adventurer.x,adventurer.y])
            pygame_screen.blit(arrow.img,[arrow.x,arrow.y])
        pygame_screen.blit(hero_image,[theHero.x,theHero.y])
        

        arrow_hit = groupcollide(arrows,bad_guys,True,True)
        # print arrow_hit
        if arrow_hit:
            bad_guys.add(BadGuy())

    if game_start == False:
        # print "Welcome" + user_name
        start_button.setup_message(user_name)
        start_button.draw_button()
        
    elif game_counter < 500:
        game_counter +=1 
        print game_counter
        print "BRAVE ONE"
        start_button2.setup_message(user_name)
        start_button2.draw_button2()
    
    pygame.display.flip()