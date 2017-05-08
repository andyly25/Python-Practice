import pygame

class Ship():

    def __init__(self, screen):
        #initialize the ship and set starting position
        self.screen = screen

        # Load the ship image and get its rect using pygame.image.load('')
        # function returns a surface representing the ship
        # NOTE: dimensions seems to be 60 x 48 pixels
        # since I changed 1200x800 to 1100x700 it is now 55x42
        self.image = pygame.image.load('images/space_ship.bmp')
        # we use get_rect() to access the surface's rect attribute
        # Pygame treat game elements like rectangles.
        # It's nice since rectangles are nice geometric shapes.
        # you can use the x and y coord of T, B, Left, Right edges of rect and
        # center to determine position of rect.
        # pygame origin (0,0) is top left corner of screen
        self.rect = self.image.get_rect()
        # store the screen's rect into self.screen_rect
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        # self.rect.centerx is the x-coordinate of ship's center.
        # by matching self.rect.centerx match centerx attribute of screen rect
        self.rect.centerx = self.screen_rect.centerx
        # Make the value of self.rect.bottom (y-coordinate of ship's bottom)
        # equal to the value of screen rect's bottom attribute.
        # pygame will use these rect attributes to pos the ship image 
        # so it's centered horiz. and aligned with bottom of screen.
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # draw the ship at its current location specified by self.rect
        self.screen.blit(self.image, self.rect)
