# Let's talk about collisions and many more interesting things
# ****************************************************************************

'''
# how things collide

import pygame
import sys
import random


pygame.init()

class Game:
    def __init__(self):

        # Screen properties
        self.screen = pygame.display.set_mode((1100,700))
        self.bg_color = (125,150,150)
        self.screen_rect = self.screen.get_rect()

        # image properties
        self.normalimage = pygame.image.load('IMAGES/2.jpg')
        self.image = pygame.transform.scale(self.normalimage, (100,100))
        self.rect = self.image.get_rect()

        # enemy_properties
        # Here we imported another object to which our object will collide and we loads it's image and transform it's scale to 50x50 and made it rect to place it midbottom
        self.normalenemy = pygame.image.load('IMAGES/1.jpg')
        self.eimage = pygame.transform.scale(self.normalenemy, (50,50))
        self.enemy_rect = self.eimage.get_rect()
        self.enemy_rect.midbottom = self.screen_rect.midbottom

        # speed properties
        self.speed = 300

        # positioning the image
        self.rect.center = self.screen_rect.center

        # Moving Flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # clock for FPS
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            dt = self.clock.tick(120) /1000
            self.events()
            self.update(dt)
            self.draw()
            if self.enemy_rect.colliderect(self.rect):
                
                # Game will freeze everytime 2 game objects collide for 200ms
                pygame.time.delay(200)
                self.enemy_rect = self.avaliable_space()
                
    def avaliable_space(self):

        # Screen width and height called out from screenrect size command
        screen_width, screen_height = self.screen_rect.size
        
        # enemy width and height called with it's rect's size
        enemy_width = self.enemy_rect.width
        enemy_height = self.enemy_rect.height

        # newx and y are new x, y random postions where our enemy will respawn
        new_x = random.randint(0, screen_width - enemy_width)
        new_y = random.randint(0, screen_height - enemy_height)

        # it is returned to the function caller in run()
        return pygame.Rect(new_x, new_y, enemy_width, enemy_height)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _keydown_event(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.moving_down = True

        elif event.key == pygame.K_LEFT:
            self.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.moving_right = True
    
    def _keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.moving_down = False

        elif event.key == pygame.K_LEFT:
            self.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.moving_right = False


    def update(self, dt):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed*dt
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.x += self.speed*dt 
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed*dt  
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed*dt  


    def draw(self):
        self.screen.fill(self.bg_color)

        # Both of the images were blit on the screen and later flipped
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.eimage, self.enemy_rect)
        pygame.display.flip()

if __name__ == '__main__':
    coll = Game()
    coll.run()'''


# *****************************************************************************************************
""" Adding the font rendering for score and make that score +=1 after every hit"""
'''import pygame
import sys
import random

pygame.init()

class Game:
    def __init__(self):
        
        self.screen = pygame.display.set_mode((1100,700))
        self.bg_color = (125,150,150)
        self.screen_rect = self.screen.get_rect()

        self.normalimage = pygame.image.load('IMAGES/2.jpg')
        self.image = pygame.transform.scale(self.normalimage, (100,100))
        self.rect = self.image.get_rect()

        self.normalenemy = pygame.image.load('IMAGES/1.jpg')
        self.eimage = pygame.transform.scale(self.normalenemy, (50,50))
        self.enemy_rect = self.eimage.get_rect()
        self.enemy_rect.midbottom = self.screen_rect.midbottom

        self.speed = 300

        self.rect.center = self.screen_rect.center

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.clock = pygame.time.Clock()
        self.score = 0
    
    def run(self):
        while True:

            dt = self.clock.tick(120) /1000
            self.events()
            self.update(dt)
            self.draw()

            if self.enemy_rect.colliderect(self.rect):
                # Game will freeze everytime 2 game objects collide for 200ms
                pygame.time.delay(50)

                # This will add sound on collision if we have already stored sount effect
                # sound = pygame.mixer.Sound("boom.wav")
                # sound.play()
                
                self.enemy_rect = self.avaliable_space()
                self.score += 1

    def avaliable_space(self):

        # Screen width and height called out from screenrect size command
        screen_width, screen_height = self.screen_rect.size
        
        # enemy width and height called with it's rect's size
        enemy_width = self.enemy_rect.width
        enemy_height = self.enemy_rect.height

        # newx and y are new x, y random postions where our enemy will respawn
        new_x = random.randint(0, screen_width - enemy_width)
        new_y = random.randint(0, screen_height - enemy_height)

        # it is returned to the function caller in run()
        return pygame.Rect(new_x, new_y, enemy_width, enemy_height)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _keydown_event(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.moving_down = True

        elif event.key == pygame.K_LEFT:
            self.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.moving_right = True
    
    def _keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.moving_down = False

        elif event.key == pygame.K_LEFT:
            self.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.moving_right = False


    def update(self, dt):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed*dt
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.x += self.speed*dt 
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed*dt  
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed*dt  


    def draw(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.eimage, self.enemy_rect)
        font = pygame.font.Font(None, 33)
        text = font.render(f"Score: {self.score}", True, (255,155,155))
        self.screen.blit(text, (10,10))
        pygame.display.flip()

if __name__ == '__main__':
    coll = Game()
    coll.run()'''



# Spawn multiple enemies randomly on the screen
# *****************************************************************************************************

# Firstly make a empty list which will be containing the every enemy object which is randomly formed


# First of all import all the important modules that will be used here
import pygame
import sys
import random
# from pygame.sprite import Sprite

# initialize the pygame
pygame.init()

# Class named Game is created
class Game:
    def __init__(self):
        
        # Screen of width and height created here
        self.screen = pygame.display.set_mode((1100,700))
        # color set
        self.bg_color = (125,150,150)
        # screen converted to a rect
        self.screen_rect = self.screen.get_rect()

        # image loaded of default size
        self.normalimage = pygame.image.load('IMAGES/2.jpg')

        # it was reduced to 100 x 100 size
        self.image = pygame.transform.scale(self.normalimage, (100,100))

        # image was converted to rect
        self.rect = self.image.get_rect()

        # enemy's image reloaded
        self.normalenemy = pygame.image.load('IMAGES/1.jpg')

        # enemy's image transformed
        self.eimage = pygame.transform.scale(self.normalenemy, (50,50))

        # enemy converted to rect
        self.enemy_rect = self.eimage.get_rect()

        # placed to midbottom
        self.enemy_rect.midbottom = self.screen_rect.midbottom

        # speed of the ship declared
        self.speed = 300

        # image's rect placed on center
        self.rect.center = self.screen_rect.center

        # Moving flags declared to false
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # self.clock named parameter takes the pygame Clock class from pygame's time
        self.clock = pygame.time.Clock()

        # Score bydefault set to 0 and will be increased by 1 every hit from main image to enemy
        self.score = 0

        # a list of enemy is made which will store enemy after respawn
        self.enemies = [self.avaliable_space()]
        
        # both says that 
        # last_hit_time = stores the timestamp of the last valid collision
        self.last_hit_time = 0
        # hit_cooldown sets the minimum wait time between two collisions
        self.hit_cooldown = 200
        # Together they both prevent repeated hits from being counted while the player and enemy overlaps continuesly
    

    # main method which will run the events, updates, draw and checkout the collisions
    def run(self):

        # While
        while True:
            
            # dt is the variable which will contain the fps controller of the game, 
            # like we have set tick to 120, means 120 Frames per second and to check how many frames in seconds, we divide 120 (fps) with 1000 (1s = 1000ms) and we get something like 0.008 secs per frame
            dt = self.clock.tick(120) /1000

            # other methods were called in while loop which will run along with true loop
            self.events()
            self.update(dt)
            self.draw()
            
            # we ran a loop on self.enemies named parameter
            for enemy in self.enemies[:]:

                # now will store the time right now
                now = pygame.time.get_ticks()  # current time in ms
                # if collision condition with enemy and the time remaining last hit time is greater than hit cool down after subtracting it from now is true, add +1 score to self.scores 
                # TL;DR if the if condition is true, it will run handle_condition method which will add +=1 to self.scores 
                if self.rect.colliderect(enemy) and now - self.last_hit_time > self.hit_cooldown:
                    self.handle_collision(enemy)

                    #  self.last_hit_time = now → records the timestamp of the latest collision so the game knows when the next one can be counted
                    self.last_hit_time = now
                    break

    # handle collision takes two parameters
    def handle_collision(self, enemy):
        # add 1 to self.score
        self.score += 1

        # This piece of lines will give the died enemy a new random place to born at x and y position
        enemy.x = random.randint(0, self.screen_rect.width - enemy.width)
        enemy.y = random.randint(0, self.screen_rect.height - enemy.height)

    def avaliable_space(self):
        # Screen width and height called out from screenrect size command
        screen_width, screen_height = self.screen_rect.size
        
        # enemy width and height called with it's rect's size
        enemy_width = self.enemy_rect.width
        enemy_height = self.enemy_rect.height

        # newx and y are new x, y random postions where our enemy will respawn
        new_x = random.randint(0, screen_width - enemy_width)
        new_y = random.randint(0, screen_height - enemy_height)

        # it is returned to the function caller in run()
        return pygame.Rect(new_x, new_y, enemy_width, enemy_height)

    # These are just events, which will work as their methods are called inside the events methods
    def events(self):

        # if x is pressed, game window will be quitted
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # as key is downed or pressed
            elif event.type == pygame.KEYDOWN:
                # call special keydown event method
                self._keydown_event(event)

            # Same here opposite
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    #Flags Set to true as their keys are pressed
    def _keydown_event(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.moving_down = True

        elif event.key == pygame.K_LEFT:
            self.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.moving_right = True
    
    # Flags set to false as keys set free or released
    def _keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.moving_down = False

        elif event.key == pygame.K_LEFT:
            self.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.moving_right = False

    # In the method update 2 parameters are passed one will give it access to dt (delta time) other is self
    def update(self, dt):
        # everytime if is used bcoz we can press two buttons like left and up, it will make it move top left diagonally

        # if self.moving left is true as well as x coordinate of self.rect(main image) is > 0, move the x of self.rect by subtracting self.speed which was declared in __init__ with product of dt .. dt will do nothing but give this a constant movement as per this supports the fps and will maintain to it and will also adjust if this same code is ran on highend computer
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed*dt
        
        # if movingright is true as well as right side of image is less than screen width, it will move until it reaches it's same width
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.x += self.speed*dt 

        # if rect's top is > 0 (0,0 are origin from top left corner) move up
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed*dt  
        
        # if the bottom is < screen height, move down
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed*dt  

    # This method will contain some stuff 
    def draw(self):
        # like adding colors by filling it on screen
        self.screen.fill(self.bg_color)

        # form the image on it's rect
        self.screen.blit(self.image, self.rect)

        # for every enemy in self.enemy, it will blit enemy too
        for enemy in self.enemies:
            self.screen.blit(self.eimage, enemy)

        # Add font to write score, enemies
        # Style is none, size is 33
        font = pygame.font.Font(None, 33)

        # text named variable stores the score and enemies like an image, and their selfs are written, true makes the edges cool, color of the text
        text = font.render(f"Score: {self.score} | Enemies: {len(self.enemies)}", True, (255,155,155))
        # form it too at 10,10 (x,y)
        self.screen.blit(text, (10,10))
        # flip the display
        pygame.display.flip()


# Run the program if it is not imported or if it is main
if __name__ == '__main__':
    coll = Game()
    coll.run()