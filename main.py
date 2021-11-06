import pygame

# need to make a surface
# convention to use caps for your constant variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!") # to give a title to the pop-up window

WHITE = (255,255,255)

def draw_window():
    WIN.fill(WHITE)  # to fill the entire space
    pygame.display.update() # we have to manually update the screen after making changes
            


# Creating your main loop
def main():
    run = True # this will be an infinite loop until we stop it
    while run:
        for event in pygame.event.get(): # this a list of all events happening in pygame
            if event.type == pygame.QUIT:
                run = False
        
        draw_window() # good practice to separate out images from the logic of the game
    
    pygame.quit()

# this makes sure that this function is run ONLY if this file is run directly.
# __name__ is just the name of the file
if __name__ == "__main__":
    main()

