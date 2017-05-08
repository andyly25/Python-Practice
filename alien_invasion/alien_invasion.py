# contains the functionality needed to make the game
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize pygame, settings, and screen object
    pygame.init()
    # create a display window called screen to draw all of game's
    # graphical elements. The tuple (1200,800) is dimension of window
    # the screen object is called a surface that displays game elements
    # when game loop activated, surface redrawn at every pass of loop
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    #Start the main loop of the game
    # an event is an action that user performs while playing
    # to make program respond, need to write event loop to listen and 
    # respons appropiately. 
    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        

run_game()


########
# NOTE: I stopped at Chapter 12, Piloting the ship