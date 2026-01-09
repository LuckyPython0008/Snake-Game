import pygame
import sys
import random

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

FRUIT_SIZE = 40
SNAKE_SIZE= 70

SCREEN_COLOR = (231,22,14)
FRUIT_COLOR = (0,255,100)

SPEED = 1

pygame.init()
class snake:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake game")
        self.screen_Rect = self.screen.get_rect()

        self.normal_image = pygame.image.load('IMAGES/2.jpg')
        self.image = pygame.transform.scale(self.normal_image, (SNAKE_SIZE, SNAKE_SIZE))
        
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_Rect.midbottom

        self.moving_up = False   
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.snake = [self.rect]
        self.positions = [self.rect.topleft]

        self.just_ate = False
        self.is_on_snake = False
        

        self.spawn_food()

        self.direction = 'UP'

        self.score = 1
    def run(self):
        while True:
            self.events()
            self.update_pos()
            self.draw()
            self.collision()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            if self.direction != 'DOWN':
                self.direction = 'UP'
        
        elif event.key == pygame.K_DOWN:
            if self.direction != 'UP':
                self.direction = 'DOWN'

        elif event.key == pygame.K_LEFT:
            if self.direction != 'RIGHT':
                self.direction = 'LEFT'

        elif event.key ==  pygame.K_RIGHT:
            if self.direction != 'LEFT':
                self.direction = 'RIGHT'
        
        elif event.key == pygame.K_q:
            sys.exit()

    def spawn_food(self):
        while True:
            x = random.randint(0, SCREEN_WIDTH - FRUIT_SIZE)
            y = random.randint(0, SCREEN_HEIGHT - FRUIT_SIZE)
            possible_fruit = pygame.Rect(x,y,FRUIT_SIZE,FRUIT_SIZE)
            is_on_snake = False
            for seg in self.snake:
                if possible_fruit.colliderect(seg):
                    is_on_snake = True
                    break

            if not is_on_snake:
                self.food = possible_fruit
                break
                

    def update_pos(self):
        dx, dy = 0,0
        if self.direction == 'UP':
            dy = -SPEED

        elif self.direction == 'DOWN':
            dy = SPEED

        elif self.direction == 'LEFT':
            dx = -SPEED

        elif self.direction == 'RIGHT':
            dx = SPEED

        if dx != 0 or dy != 0:
            self.rect.x += dx
            self.rect.y += dy
            
            self.rect.clamp_ip(self.screen_Rect)
            self.positions.insert(0, self.rect.topleft)

            if len(self.positions) > len(self.snake) * FRUIT_SIZE:
                self.positions.pop()

            for i, seg in enumerate(self.snake):
                step = i * FRUIT_SIZE
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
        # Existance of snake
        self.screen.fill(SCREEN_COLOR)
        for snake_obj in self.snake:
            self.screen.blit(self.image, snake_obj)

        # Existance of the font, score
        font = pygame.font.Font(None, 40)
        text = font.render(f"Score: {self.score}", True, (0,0,255))
        self.screen.blit(text, (20,10))
        

        # drawing fruit for snake
        pygame.draw.rect(self.screen, FRUIT_COLOR, self.food)
        pygame.display.flip()

if __name__ == '__main__':
    snak = snake()
    snak.run()
    

