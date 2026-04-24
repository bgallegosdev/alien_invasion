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
from bullet import Bullet
from alien import Alien
# pygame.version.ver

class AlienInvasion:
    """ Overall class for our game """

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode( ( self.settings.screen_width, self.settings.screen_height ) )
        pygame.display.set_caption( "Alien Invasion" )
        self.ship = Ship( self )
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()            
            self._update_screen()

    def _create_fleet(self):
        ''' Create a fleet of aliens '''
        # Create an alien and find number in rows
        # Spacing between each alien is one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - ( 2 * alien_width )
        number_aliens_x = available_space_x // ( 2 * alien_width)

        # Determine how many rows that will fit in the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             ( 3 * alien_height ) - ship_height)
        number_rows = available_space_y // ( 2 * alien_height )

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien( alien_number, row_number )

    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it
        alien = Alien( self )
        alien_width, alien_height = alien.rect.size
        # alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add( alien )

        # # Make an alien
        # alien = Alien(self)
        # self.aliens.add( alien )

    def _update_bullets(self):
        ''' Update position of bullets and get rid of strays  '''
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullet that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print( len(self.bullets) )

    def _update_screen(self):
        # Redraw the screen during each pass of the loop
        self.screen.fill( self.settings.bg_color )
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visable
        pygame.display.flip()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        ''' Responds to keypresses up. '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        ''' Responds to keypresses down. '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        ''' Create a new bullet & add to group '''
        if len(self.bullets)  < self.settings.bullets_allowed:
            new_bullet = Bullet( self )
            self.bullets.add( new_bullet )
        

if __name__ == "__main__":
        # Make the game instance and run the game
        ai = AlienInvasion()
        ai.run_game()
