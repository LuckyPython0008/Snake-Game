import pygame
import sys
import random

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1100

BG_COLOR = (100,160,120)

class snake:
    def __init__(self):
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

        self.rect.midbottom = self.screen_rect.midbottom

    def run(self):
        dt = self.clock.tick(120)/1000
        while True:
            self.events()
            self.update_pos(dt)
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
            

    def update_pos(self, dt):

        # Keep these in the if-else statement if you want it to make them move in only left, right, up and down

        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed * dt

        elif self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.rect.y += self.speed * dt

        elif self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed * dt

        elif self.moving_right and self.rect.right < self.screen_rect.width:
            self.rect.x += self.speed * dt


        # Keep it only in if, if you want to move them diagonally too
        # if self.moving_up and self.rect.top > 0:
        #     self.rect.y -= self.speed * dt

        # if self.moving_down and self.rect.bottom < self.screen_rect.height:
        #     self.rect.y += self.speed * dt

        # if self.moving_left and self.rect.x > 0:
        #     self.rect.x -= self.speed * dt

        # if self.moving_right and self.rect.right < self.screen_rect.width:
        #     self.rect.x += self.speed * dt

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

if __name__ == '__main__':
    head_move = snake()
    head_move.run()