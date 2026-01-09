import pygame
import sys
import random

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1100

BG_COLOR = (100,160,120)

class snake:
    def __init__(self):

        # We must have a screen to make things happen and the variables who contain width and height were already declared outside the class snake
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        # IMAGE SETTINGS
        self.normal_image = pygame.image.load('IMAGES/3.jpg')
        self.image = pygame.transform.scale(self.normal_image, (80,80))
        self.rect = self.image.get_rect()

        # SPEED SETTINGS
        self.speed = 100

        # MOVING FLAGS
        self.moving_up = False 
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # fps clock
        self.clock = pygame.time.Clock()

        # positioned the rect at the bottom of the screen or else the snake will appear on topleft (in origin)
        self.rect.midbottom = self.screen_rect.midbottom

        # Fruit size so make something for snake to eat
        self.fruit_size = 40

        # spawn food called in __init__ so that it is called automatically
        self.spawn_food()

        # Self.snake is the list of the snake segments
        self.snake = [self.rect]

        # self.positions store the position of each segment as the snake grows after eating the fruit
        self.positions = [self.rect.topleft]

        # flag set for either the fruit is eaten or not
        self.just_ate = False

        # score bydefault is set to one, bcoz we can see the number of snake chunks we got after alot of fruits being eaten
        self.score = 1

    def run(self):

        # delta time to store time taken for per sec if the fps is 120
        dt = self.clock.tick(120)/1000
        while True:

            # All usable methods called inside the While True method
            self.events()
            self.update_pos(dt)
            self.draw()
            self.collision()

    # Event method
    def events(self):

        # Pygame library, itself has module called event, and we looped over it and checked weather the following if, elif conditions are true
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    # keydown events method takes two parameters, one is self and other is the event (event for that event module in pygame library)
    def _keydown_events(self, event):

        # Here, based on every key up, down, left, right button is key_down their respective flag is set to true
        if event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.moving_right = True

    def _keyup_events(self, event):
        # and everytime the any key is up, their flag is set to false again
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.moving_right = False

    # spawn food is the method which we called inside __init__ , it just decide randomly that where should the food must spawn randomly after the fruit is eaten
    def spawn_food(self):

        # x, y are the random coordinates from the surface
        x = random.randint(0, SCREEN_WIDTH - self.fruit_size)
        y = random.randint(0, SCREEN_HEIGHT - self.fruit_size)

        # self.food varible store the actual food which is created from the rect , with the following x, y and their sizes 
        self.food = pygame.Rect(x,y, self.fruit_size, self.fruit_size)

    def update_pos(self, dt):
        dx, dy = 0,0

        if self.moving_up == True:
            dy = -self.speed * dt
        
        elif self.moving_down == True:
            dy = self.speed * dt

        elif self.moving_left == True:
            dx = -self.speed * dt

        elif self.moving_right == True:
            dx = self.speed * dt


        if dx != 0 or dy!= 0:
            self.rect.x += dx
            self.rect.y += dy

            # rect_to_clamp.clamp_ip(bounding_rect)
            self.rect.clamp_ip(self.screen_rect)

            self.positions.insert(0, self.rect.topleft)
        
            if len(self.positions) > len(self.snake) * self.fruit_size:
                self.positions.pop()

            for i, seg in enumerate(self.snake):
                step = i * self.fruit_size
                if step < len(self.positions):
                    seg.topleft = self.positions[step]

            if self.just_ate: 
                new_seg = self.image.get_rect(topleft = self.positions[-1])        
                self.snake.append(new_seg)
                self.just_ate = False

    def collision(self):
        if self.snake[0].colliderect(self.food):
            self.score += 1
            self.spawn_food()
            self.just_ate = True

    def draw(self):
        self.screen.fill(BG_COLOR)
        # self.screen.blit(self.image, self.rect)
        for segment in self.snake:
            self.screen.blit(self.image, segment)
        pygame.draw.rect(self.screen, (255,200,0), self.food)

        font = pygame.font.Font(None, 33)
        text = font.render(f"Score: {self.score}", True, (255,0,255))
        self.screen.blit(text, (10,10))


        pygame.display.flip()

if __name__ == '__main__':
    head_move = snake()
    head_move.run()