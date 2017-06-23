"""GameWindow.py
This is the main game window.
It provides the main game functionality.
"""
#import section
import pygame
import eztext
import sys
from pygame.locals import *

#global variables initialization

    #screen size
win_width= 800
win_height =600

    #colors
black= (0, 0, 0)
grey=(100,100,100)
white= (255, 255, 255)
red= (255, 0, 0)
green= (0, 255, 0)
blue= (0, 0, 255)
gray=(64, 64, 64)

#pygame init
pygame.init()
    #pygame variables
window=pygame.display.set_mode((win_width, win_height))
textbox= eztext.Input(maxlength=40, color= black, prompt="What do you do?: " )
clock = pygame.time.Clock()
#background
background= pygame.Surface((win_width, win_height))
background.fill(grey)
#surfaces
graphicwin =pygame.Surface((win_width*0.8,win_height *0.88))
graphicwin.fill(black)
textsurf=pygame.Surface((win_width*0.98, win_height *0.10))
textsurf.fill(white)
statusbar =pygame.Surface((win_width*0.19, win_height*0.88))
textbox.draw(textsurf)
#font
gamefont= pygame.font.SysFont('Gothic', 12)

def RunWindow() :
    """This is the main graphic loop.
    It keeps the game running.
    """
    
    while True :
        clock.tick(30)

        events = pygame.event.get()
        #event list
        for event in events:
            if event.type == QUIT:
                return
        window.blit(background, (0,0))
        window.blit(statusbar, (0, 0))
        window.blit(graphicwin,(0.2*win_width, 0))
        textbox.update(events)
        text = textbox.get()
        textbox.draw(textsurf)
        window.blit(textsurf, (0, 0.9*win_height))

        pygame.display.update()
        
#####END Function
        
if __name__ == '__main__': RunWindow()  



