import pygame
import os  # to help us define the path to these images

# need to make a surface
# convention to use caps for your constant variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!") # to give a title to the pop-up window

WHITE = (255,255,255)

FPS = 60 # defining the refreshing rate at 60 frames per second
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

def draw_window(red,yellow):
    WIN.fill(WHITE)  # to fill the entire space ...
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # we're feeding the values for the rectangles "red" and "yellow" below with coordinates
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update() # we have to manually update the screen after making changes.

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
# to resize the image (which you need to embed in a rotate command)
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),(90))

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),(270))



# Creating your main loop
def main():
    # we'll pass these rectangles over to draw_window()
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # x, y, width, height
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock() # creating a clock object in this loop
    run = True # this will be an infinite loop until we stop it
    
    while run:
        clock.tick(FPS) # this makes sure that the while loop runs 60 times per second.
        for event in pygame.event.get(): # this a list of all events happening in pygame
            if event.type == pygame.QUIT:
                run = False
        
        red.x += 1
        draw_window(red, yellow) # good practice to separate out images from the logic of the game
    
    pygame.quit()

# this makes sure that this function is run ONLY if this file is run directly.
# __name__ is just the name of the file
if __name__ == "__main__":
    main()

