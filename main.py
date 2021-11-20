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
VEL = 5 # a variable of velocity of the ships= 5
BULLET_VEL = 7 # velocity for the projectiles
MAX_BULLETS = 50
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
    if keys_pressed[pygame.K_LEFT] and red.x + VEL - red.width > BORDER.x + BORDER.width - 30:             # arrow keys need to be caps
        red.x -= VEL # subract from our x value to move
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width - 5 < WIDTH:             # makes 'd' the right movement
        red.x += VEL # adds to our x value to move
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:           
        red.y -= VEL # UP  (remember, the 0 is in the top left corner)
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height + 10 < HEIGHT:             
        red.y += VEL # DOWN

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullets in yellow_bullets:
        bullet.x += BULLET_VEL  # to move yellow's bullets to the right 
            if yellow.colliderect(bullet)  # this tool tells us if bullets have collided with the rectangle "yellow"
            # you need to post an event that the collision happened
                yellow_bullets.remove(bullet) #logically, if the collision happens, the bullet goes away
    
    for bullets in red_bullets:
        bullet.x -= BULLET_VEL  # to move red's bullets to the right 


# Creating your main loop
def main():
    # we'll pass these rectangles over to draw_window()
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # x, y, width, height
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # to create projectiles in the game:
    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock() # creating a clock object in this loop
    run = True # this will be an infinite loop until we stop it
    
    while run:
        clock.tick(FPS) # this makes sure that the while loop runs 60 times per second.
        for event in pygame.event.get(): # this a list of all events happening in pygame
            if event.type == pygame.QUIT:
                run = False
        
            # to create the bullets:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)  # so that the bullet is fired from the ship (height/2 puts it in the middle)
                    yellow_bullets.append(bullet)    # the 10 and 5 are the height and width of the bullets

                if event.key == pygame.K_m and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 - 2, 10, 5)  # we don't need to add the width like for yellow, becuase red is firing to the left
                    red_bullets.append(bullet)  

        print (red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed() # with every loop it will tell us which keys are being pressed down.
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        # another function for bullets
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        
        draw_window(red, yellow) # good practice to separate out images from the logic of the game
    
    pygame.quit()

# this makes sure that this function is run ONLY if this file is run directly.
# __name__ is just the name of the file
if __name__ == "__main__":
    main()

