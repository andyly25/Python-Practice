# we use this module to exit the game when user quits
import sys

import pygame

def check_events():
    #watch for keyboard and mouse events
    # inside will have series of if statements to respond to specific 
    # events. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make the recently drawn screen visible. Creates an empty screen 
    #each time through while loop to erase old screen for new.
    pygame.display.flip()