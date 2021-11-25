import pygame
import os  # to help us define the path to these images
pygame.font.init() # to draw fonts on the screen

# need to make a surface
# convention to use caps for your constant variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!") # to give a title to the pop-up window

WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)# to create borders to prevent ships from colliding; two slashes for floating point division
                                                # we wanted the x to be in the middle of the screen
                                                # it's -5 because you want it to be half the width of the whole shape

# to draw fonts on the screen:
HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

# for the "firings":
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2 # this can't be '1" because otherwise they'd be the same event

FPS = 60 # defining the refreshing rate at 60 frames per second
VEL = 5 # a variable of velocity of the ships= 5
BULLET_VEL = 7 # velocity for the projectiles
MAX_BULLETS = 50
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health): # these are the entities drawn on the canvas
    WIN.blit(SPACE, (0,0)) # to fill the canvas with 'space,' and we already know the dimensions ...
    pygame.draw.rect(WIN, BLACK, BORDER)  # drawing a rectangle, but not pygame.Rect()
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10)) # will blit the health into the top left of the screen, with 10 pixels on the y as padding
    WIN.blit(yellow_health_text, (10,10)) # easy: on the extreme left of the screen, we just need a buffer of 10 from the left and 10 from the top

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # we're feeding the values for the rectangles "red" and "yellow" below with coordinates
    WIN.blit(RED_SPACESHIP, (red.x, red.y)) 

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet) # "drawing a red rectangle called "bullet" on the screen"
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet) # "drawing a red rectangle called "bullet" on the screen"
    

    pygame.display.update() # we have to manually update the screen after making changes.

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
# to resize the image (which you need to embed in a rotate command)
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),(90))

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),(270))

# to load (and resize) the prepared background:
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

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
    if keys_pressed[pygame.K_LEFT] and red.x + VEL - red.width > BORDER.x + BORDER.width - 30:  # arrow keys need to be caps
        red.x -= VEL # subract from our x value to move
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width - 5 < WIDTH: # makes 'd' the right movement
        red.x += VEL # adds to our x value to move
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:           
        red.y -= VEL # UP  (remember, the 0 is in the top left corner)
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height + 10 < HEIGHT:             
        red.y += VEL # DOWN

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL  # to move yellow's bullets to the right 
        if red.colliderect(bullet):  # this tool tells us if bullets have collided with the rectangle "red"
            # you need to post an event that the collision happened
            pygame.event.post(pygame.event.Event(RED_HIT))   # except for RED_HIT, what the ... ??
            yellow_bullets.remove(bullet) #logically, if the collision happens, the bullet goes away
        elif bullet.x > WIDTH: # if the bullets go off the screen, then disappear
            yellow_bullets.remove(bullet) 

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL  # to move red's bullets to the right 
        if yellow.colliderect(bullet):  # this tool tells us if bullets have collided with the rectangle "yellow"
            # you need to post an event that the collision happened
            pygame.event.post(pygame.event.Event(YELLOW_HIT))   # except for RED_HIT, what the ... ??
            red_bullets.remove(bullet) #logically, if the collision happens, the bullet goes away
        elif bullet.x < 0:  # going the opposite direction
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    # this will put the winner announcement directly in the middle of the screen (first the x, then the y)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2)) 
    pygame.display.update()
    pygame.time.delay(5000) # we show the tet for 5 seconds and then restart the game.


# Creating your main loop
def main():
    # we'll pass these rectangles over to draw_window()
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # x, y, width, height
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # to create projectiles:
    red_bullets = []
    yellow_bullets = []

    # to keep track of hits during game play:
    red_health = 10
    yellow_health = 10

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
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)  # so that the bullet is fired from the ship (height/2 puts it in the middle, two slashes for integer division)
                    yellow_bullets.append(bullet)    # the 10 and 5 are the height and width of the bullets

                if event.key == pygame.K_m and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)  # we don't need to add the width like for yellow, becuase red is firing to the left
                    red_bullets.append(bullet)  

            if event.type == RED_HIT:  # we're just thsi particular event to the queue of other possible events
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1
        
        winner_text = ""  # sets up a blank string
        if red_health <= 0:
            winner_text = "Yellow wins!!"
        if yellow_health <= 0:
            winner_text = "Red wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed() # with every loop it will tell us which keys are being pressed down.
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        # another function for bullets
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # good practice to separate out images from the logic of the game
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health) 


    pygame.quit()

# this makes sure that this function is run ONLY if this file is run directly.
# __name__ is just the name of the file
if __name__ == "__main__":
    main()

