import sys
import pygame   
def run_game():
    screen=pygame.display.set_mode((600,400))
    pygame.display.set_caption()
   
    while True:
        for event in pygame.event.get():
            pygame.ass=input("enter your name")
            
            if pygame.QUIT==ass:
             sys.exit()
run_game()             

from settings import Settings
from ship import Ship
def run_game():
 
 pygame.display.set_caption("Alien Invasion")
 # Make a ship.
 ship = Ship(screen)
 # Start the main loop for the game.
 while True:

 # Redraw the screen during each pass through the loop.
  screen.fill(ai_settings.bg_color)
  ship.blitme()
 
 # Make the most recently drawn screen visible.
 pygame.display.flip()
run_game()