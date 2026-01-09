'''import pygame
import sys
# pygame and sys were imported because pygame is a module which carries all the important stuff related to building games and putting up the game screen, sys is called to exit the game

pygame.init()
# This piece of shit reloads all the rounds from the mag called pygame so we can use it realistically.


# This writes the title of the screen on the top of the window
pygame.display.set_caption("Yellow window")

screen = pygame.display.set_mode((500,500))
# Screen, so clear, just set width, height respectively and make that dumb screen

color = (255,255,0)
#Set the color of the screen you like 

# While loop runned, to put some functions in it
while True:

    # there are so many events in pygame.event and event means any activity performed on the game screen is event, even if it is mouse button clicked, or cursor is moved, and from all those activities, we run for loop and get one event called QUIT, and used sys to exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # We declared color in a tuple, in R G B format, and screen is filled with the color
    screen.fill(color)

    # flip, an important part, it does the main job to show the latest screen or what was drawn from the last time, it just update the screen and show what was drawn on screen since last update
    pygame.display.flip()
'''

# ***************************************************************************************


'''
# Now let's add the image and put it anywhere on the screen

import pygame
import sys

pygame.init()

# Making surface
screen = pygame.display.set_mode((700,700))
color = (255,255,90)
# Making it a rect, (rect is the short form of rectangle) and we assume every object in pygame a rectangle, some are big, some are small, according to their sizes, rectangles are the best way to make interaction with them possible, these are not actually visible but they are there and perform specific tasks.. 
screen_rect = screen.get_rect()

# now let's add the image on the screen
normalimage = pygame.image.load('IMAGES/1.jpg')

# You can even transform this image by its size
image = pygame.transform.scale(normalimage, (100,100))
image_rect = image.get_rect()

# Set the image position midbottom compare to the rect of the screen
image_rect.midbottom = screen_rect.midbottom

# you can use several method to point this object anywhere using some prebuilt methods
# image_rect.center = screen_rect.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(color)

    # Blit is nothing but a method to draw image on the surface of the required image_rect by taking the coordinated of the image's rect
    # its formula is screen.blit(image, (200,400))
    # image is the image which is to drawn and 200,400 is the position where it should be drawn with respect to it's origin, top left corner (0,0)
    screen.blit(image, image_rect)

    # Update updates the whole screen while flip can update a specific area or object while also being able to update the whole screen
    pygame.display.flip()
'''


# *********************************************************************************



            
