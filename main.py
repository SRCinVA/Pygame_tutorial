import pygame
import os  # to help us define the path to these images

# need to make a surface
# convention to use caps for your constant variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!") # to give a title to the pop-up window

WHITE = (255,255,255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)# to create borders to prevetn ships from colliding
                                                # we wanted the x to be in the middle of the screen
                                                # it's -5 because you want it to be half the width of the whole shape

FPS = 60 # defining the refreshing rate at 60 frames per second
VEL = 5 # a variable of velocity = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

def draw_window(red,yellow):
    WIN.fill(WHITE)  # to fill the entire space ...
    pygame.draw.rect(WIN, BLACK, BORDER)  # drawing a rectangle, but not pygame.Rect()
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # we're feeding the values for the rectangles "red" and "yellow" below with coordinates
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update() # we have to manually update the screen after making changes.

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
# to resize the image (which you need to embed in a rotate command)
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),(90))

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),(270))

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # makes 'a' the left movement
                                                        # Velocity might be the number of pixels (or other standard unit) per FPS
        yellow.x -= VEL # subract from our x value to move
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # makes 'd' the right movement
                                                            # the 'and' statement won't let us move beyond the border's 'x' position.
                                                            # the 'yellow.width' makes sure *none* of the spaceship can go over the right border.
        yellow.x += VEL # adds to our x value to move
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:           
        yellow.y -= VEL # UP
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10: # for some strange reason, we have to add more buffer; 
                                                                                  # by subtracting 10, we reduced the total downward latitude the spaceship has            
                                                            # the 'yellow.height' makes sure *none* of the spaceship can go over the bottom border.                                                                                                                       
        yellow.y += VEL # DOWN

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:             # arrow keys need to be caps
        red.x -= VEL # subract from our x value to move
    if keys_pressed[pygame.K_RIGHT]:             # makes 'd' the right movement
        red.x += VEL # adds to our x value to move
    if keys_pressed[pygame.K_UP]:           
        red.y -= VEL # UP  (remember, the 0 is in the top left corner)
    if keys_pressed[pygame.K_DOWN]:             
        red.y += VEL # DOWN

# Creating your main loop
def main():
    # we'll pass these rectangles over to draw_window()
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # x, y, width, height
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock() # creating a clock object in this loop
    run = True # this will be an infinite loop until we stop it
    
    while run:
        clock.tick(FPS) # this makes sure that the while loop runs 60 times per second.
        for event in pygame.event.get(): # this a list of all events happening in pygame
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed() # with every loop it will tell us which keys are being pressed down.
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow) # good practice to separate out images from the logic of the game
    
    pygame.quit()

# this makes sure that this function is run ONLY if this file is run directly.
# __name__ is just the name of the file
if __name__ == "__main__":
    main()

