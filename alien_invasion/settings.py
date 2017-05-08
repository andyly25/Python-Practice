# Each time there's a new functionality there would be specific settings, so 
# we will make a settings module to store all of the settings in one place.
# Allows to pass one settings object instead of many individual object.


class Settings():

    def __init__(self):
        #initialize the game settings

        # screen settings
        # changed width and height from 1200 x 800 to 1100 x 700
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (66,134,244)