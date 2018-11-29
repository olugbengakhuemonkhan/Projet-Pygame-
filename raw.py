# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

from age import whatAge


#def get_key():

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #             # THE USER CLICKED THE RED DOT!
    #             # These aren't the droids were looking for. quit.
    #             game_on = False
    #     elif event.type == pygame.KEYDOWN:
    #         # the user pressed a key!!!
    #         print event.key

def get_key():
    while 1:
        for event in pygame.event.get():
    
            if event.type == pygame.KEYDOWN:
                return event.key
            else:
                pass
            if event.type == pygame.QUIT:
                pygame.display.quit()
            else:
                pass    

def display_box(screen, message):

  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
#   "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  print current_string
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((512,480))
  screen_name = ask(screen, "Name")
  print screen_name + "  was entered"

if __name__ == '__main__': main()