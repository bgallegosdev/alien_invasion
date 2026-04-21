# Name: Benjamin Gallegos
# Course: Python ITSE 1359.004
# Assignment: Final Exam
# Date: April 13, 2026 (start date)
# Reference : see readme.md

# I have installed pygame
import sys # module for OS
import pygame
from settings import Settings
from ship import Ship
# pygame.version.ver

class AlienInvasion:
    """ Overall class for our game """

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode( ( self.settings.screen_width, self.settings.screen_height ) )
        pygame.display.set_caption( "Alien Invasion" )
        self.ship = Ship( self )

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        # Redraw the screen during each pass of the loop
        self.screen.fill( self.settings.bg_color )
        self.ship.blitme()

        # Make the most recently drawn screen visable
        pygame.display.flip()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
        # Make the game instance and run the game
        ai = AlienInvasion()
        ai.run_game()
