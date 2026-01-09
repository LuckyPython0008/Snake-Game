#  Learning about key presses, adding motions and organizing everything into classes and method
'''
# We'll use classes because these classes are object oriented programming and we can even work with real world things
# Modules imported successfully
import pygame
import sys

# initializing the pygame
pygame.init()

# A class named Game is created 
class Game:

    # This init method runs automatically, when object is created
    # 
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
p1 = Game('Lucky', 34)
print(p1.name, p1.score)


# ACTUAL CODE STARTS NOW
class Game:
    def __init__(self):

        # Making screen's self and making a screen
        self.screen = pygame.display.set_mode((1300,700))

        # Setting caption or title on the top of the surface
        pygame.display.set_caption("Bam o oex")

        # Making rect of the scree
        self.screen_rect = self.screen.get_rect()

        # Back ground color for Surface is assigned
        self.bg_color = (230,143,121)

        # adding image in this set
        self.normalimage = pygame.image.load('IMAGES/2.jpg')

        # Transforming it's size
        # self.image = pygame.transform.rotate(self.normalimage, 45)
        self.image = pygame.transform.scale(self.normalimage, (100,100))
        
        # Making the image a rect
        self.rect = self.image.get_rect()

        # Let's place it somewhere
        self.rect.midbottom = self.screen_rect.midbottom

    def run(self):

        while True:
            self.update()
            self.events()

    # Here we did nothing but made a function which contains all our events which will happen on the surface or game screen
    def events(self):
        # we pull out a event if it's type is QUIT, sys will exit the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # from those event we also pull out a type of event which means a key is down or key is pressed and i can set what should happen if specific key is pressed by user
            elif event.type == pygame.KEYDOWN:

                # i made another method named _keydown_event which will contain all the keydown event we need and we call it here
                self._keydown_event(event)
            
            # key up is the type of event which means when we've released already pressed keydown key
            elif event.type == pygame.KEYUP:

                # another keyup method which will contain things
                # self._keyup_event(event)
                pass
                # We don't currently need this bcoz things will work and move as keys are pressed

    # Here's our keydown event holder, it contains output of any button we press
    # To this method, or function we pass a parameter event so that we can pull out it's result in events method
    def _keydown_event(self, event):
        # we ask if event's key pressed is left arrow key K_LEFt and if x coordinates are greater than 0 then move it to left side by subtracting 1 pixel per click, self.x > 0 is used bcoz top left corner is 0, 0 origin and left side of screen is (x,y) => (0, y) so if it is greater than 0. it will be applied and will not go outside the screen
        if event.key == pygame.K_LEFT and self.rect.x > 0:

            # decrease 1 pixel from its x axis per click so it can feel like moving left
            self.rect.x -=1

        # if right key is pressed and if rightside of self.rect (object or image)is less then width of the screen's rect then it can move right
        elif event.key == pygame.K_RIGHT and self.rect.right < self.screen_rect.width:
            self.rect.x += 1

        # if q is pressed pygame will quit this screen
        elif event.key == pygame.K_q:
            pygame.QUIT
            sys.exit()

    def update(self):
        # Here we fill the screen with the color we declared in __init__ to the screen
        self.screen.fill(self.bg_color)

        # Blit makes the image form on the screen, it means put image on the self.rect, means put image on the (x,y) of the self.rect
        self.screen.blit(self.image, self.rect)

        # Show the last time updated screen
        pygame.display.flip()

#  __name__ == "__main__" means that if this condition is true, means if the file we are running is not imported from else where, then if condition comes true else it won't run
if __name__ == "__main__":
    
    ai = Game()
    ai.run()'''

# ***********************************************************************************

# Now we will add a continues motion when a key is not released after pressed


'''# Modules imported successfully
import pygame
import sys

# pygame initialize
pygame.init()

# We made a continues named class
class Continues:

    # __init__ declared so that some object's chracterstics will be automatically runned
    def __init__(self):

        # screen mode set
        self.screen = pygame.display.set_mode((1300,700))

        # we make a virtual rect around that screen
        self.screen_rect = self.screen.get_rect()

        # set its color
        self.bg_color = (122,144,166)

        # Set it's caption 
        pygame.display.set_caption("Continues motion on key press hold")

        # we add a image here
        self.normal_image = pygame.image.load('IMAGES/3.jpg')

        # It was too big for screen, so we reduced it's size
        self.image = pygame.transform.scale(self.normal_image, (100,100))

        # Make rect of photo
        self.rect = self.image.get_rect()

        # Place the photo somewhere, like midbottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Now the main part, we put the flags here to false and they will be declared to True in the event.key to true
        self.moving_left = False
        self.moving_right = False

    # We made another method named run, to run events and updates till the condition or game is running
    def run(self):
        while True:
            self.event()
            self.update()

    # Another event named class which run the for loop for event
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # we made seperate method for this keydown event to put all the keydown events in that named _keydown_event(event)
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            
            # Same for this but keyup
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    # Keydown events start here which will contain several keydown events
    def _keydown_event(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_LEFT:
            # Here we set flag to moving left to true
            self.moving_left = True

        elif event.key == pygame.K_RIGHT:
            # Here we set flag to moving right to true
            self.moving_right = True

    def _keyup_event(self, event):
        if event.key == pygame.K_LEFT:

            # When key is released we immediatly put that flag to false so no further movement
            self.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.moving_right = False
        
    # Another method of flags
    def update(self):

        # Just setting the true or false won't make them move left or right, we need to put if statement and check if the object is already out of surface or not
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= 2
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 2

        # fill the screen with the declared color
        self.screen.fill(self.bg_color)

        # Make the image form on it's rect
        self.screen.blit(self.image, self.rect)

        # Flip the screen and show what's happening behind the scene
        pygame.display.flip()

# Run the program if it is not imported
if __name__ == "__main__":
    conti = Continues()
    conti.run()'''


# Let's try moving them diagonally or anywhere****************************************************

'''import pygame
import sys

pygame.init()

class Continues:

    def __init__(self):

        self.screen = pygame.display.set_mode((1300,700))

        self.screen_rect = self.screen.get_rect()

        self.bg_color = (122,144,166)

        pygame.display.set_caption("Continues motion on key press hold")

        self.normal_image = pygame.image.load('IMAGES/3.jpg')

        self.image = pygame.transform.scale(self.normal_image, (100,100))

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


    def run(self):
        while True:
            self.event()
            self.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # we made seperate method for this keydown event to put all the keydown events in that named _keydown_event(event)
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            
            # Same for this but keyup
            elif event.type == pygame.KEYUP: 
                self._keyup_event(event)

    def _keydown_event(self, event):
        if event.key == pygame.K_q:
            sys.exit()

        # Put all moving directions to true as per their required direction
        elif event.key == pygame.K_LEFT:
            self.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.moving_right = True

        elif event.key == pygame.K_UP:
            self.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.moving_down = True

    def _keyup_event(self, event):

        # Set them false as we release their button
        if event.key == pygame.K_LEFT:
            self.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.moving_right = False

        elif event.key == pygame.K_UP:
            self.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.moving_down = False
        
    # Another method of flags
    def update(self):

        # horizontal
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= 2
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 2

        # vertical
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
        
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 2

        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

# Run the program if it is not imported
if __name__ == "__main__":
    conti = Continues()
    conti.run()'''

# Setting the FPS on the screen's object movement
#************************************************************************************************

'''import pygame
import sys

pygame.init()

class FPS:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,600))
        self.bg_color = (233,244,255)
        self.screen_rect = self.screen.get_rect()

        self.normalimage = pygame.image.load('IMAGES/4.jpg')
        self.image = pygame.transform.scale(self.normalimage, (100,100))
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # Setting the speed of object to 300 pixels
        self.speed = 300

        # calling boss for maintaining the fps
        self.clock = pygame.time.Clock()

        self.rect.midbottom = self.screen_rect.midbottom
    def run(self):
        while True:

           # Here's the main thing:
# tick(120) sets the *maximum* FPS to 120, so the game loop never runs faster than that.
# It also tells us how long the last frame took to run (in milliseconds).
#
# That frame time is usually a very small number (like 16 ms at ~60 FPS).
# To convert it into seconds, we divide by 1000 (since 1 second = 1000 ms).
# We store that in 'dt' (delta time).
#
# Now, regardless of whether the PC runs at 30, 60, or 120 FPS,
# multiplying speed * dt makes the movement consistent.
# The object will move the *same distance per second* on any machine,
# giving smooth and fair motion.
            
            dt = self.clock.tick(120)/1000
            self.events()
            self.update(dt)
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.moving_right = True

    def _keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.moving_right = False
        
        # Important point is that if you put if elif statements here, if 2 keys are pressed for diagonal movement only one of them will be considred
    def update(self, dt):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed * dt 
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.x += self.speed * dt 
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed * dt 
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed * dt 

    def draw(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

if __name__ == '__main__':
    fps = FPS()
    fps.run()
    '''

# ************************************************************************************
# Only move left right up or down, no diagonal
'''
import pygame
import sys

pygame.init()

class FPS:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,600))
        self.bg_color = (233,244,255)
        self.screen_rect = self.screen.get_rect()

        self.normalimage = pygame.image.load('IMAGES/4.jpg')
        self.image = pygame.transform.scale(self.normalimage, (100,100))
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # Setting the speed of object to 300 pixels
        self.speed = 300

        # calling boss for maintaining the fps
        self.clock = pygame.time.Clock()

        self.rect.midbottom = self.screen_rect.midbottom
    def run(self):
        while True:         
            dt = self.clock.tick(120)/1000
            self.events()
            self.update(dt)
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.moving_right = True

    def _keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.moving_right = False
        
        # Important point is that if you put if elif statements here, if 2 keys are pressed for diagonal movement only one of them will be considred
    def update(self, dt):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed * dt 
        elif self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.x += self.speed * dt 
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed * dt 
        elif self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed * dt 

    def draw(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

if __name__ == '__main__':
    fps = FPS()
    fps.run()
    
'''