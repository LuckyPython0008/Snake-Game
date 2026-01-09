import pygame
import sys
import random

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700

FRUIT_SIZE = 40

SNAKE_SIZE = 70

FRUIT_COLOR = (255,0,0)
SCREEN_COLOR = (0,255,0)

SNAKE_SPEED = 30

GAP = 2
# initializing the pygame
pygame.init()

class snake:
    def __init__(self):
        # SCREEN SETTINGS
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        # SNAKE (IMAGE) SETTINGS
        self.normal_image = pygame.image.load('IMAGES/3.jpg')
        self.image = pygame.transform.scale(self.normal_image, (SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.image.get_rect()

        # POSITIONING
        self.rect.midbottom = self.screen_rect.midbottom

        # DIRECTION FLAGS
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # OVERLAPPING FRUITS FLAGS or ITSELF
        self.is_on_snake = False
        self.is_on_itself = False
        self.on_text = False

        # FPS clock
        self.clock = pygame.time.Clock()

        # DIRECTING THE SNAKE AND MAKING IT MOVEMENT CONTINUES WITHOUT KEEP PRESSING THE BUTTON
        self.direction = 'UP'

        # LIST THAT STORES SNAKE SEGMENTS OR BODY AND STORES POSITION
        self.snake = [self.rect]
        self.positions = [self.rect.topleft]

        # FRUIT EITHER EATEN OR NOT
        self.just_ate = False

        # SCORING SYSTEM
        self.score = 1

        # spawn food automatically
        self.spawn_food()

    def run(self):
        dt = self.clock.tick(60) / 1000

        while True:
            self.events()
            self.update_pos(dt)
            self.collision()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _keydown_events(self, event):
        # if keyup is pressed and the self.direction varible is not down, then go up, this will make the snake not move in opposite direction by just pressing the key
        if event.key == pygame.K_UP:    
            if self.direction != 'DOWN':
                self.direction = 'UP'

        elif event.key == pygame.K_DOWN:    
            if self.direction != 'UP':
                self.direction = 'DOWN'

        elif event.key == pygame.K_LEFT:    
            if self.direction != 'RIGHT':
                self.direction = 'LEFT'

        elif event.key == pygame.K_RIGHT:    
            if self.direction != 'LEFT':
                self.direction = 'RIGHT'

        elif event.key == pygame.K_q:
            sys.exit()
    
    # def spawn_food(self):
    #     # making food also not appear on the text, like scoreboard
    #     self.no_tresspass = pygame.Rect(0,0,100,100)
    #     while True:
    #         x = random.randint(0, SCREEN_WIDTH-FRUIT_SIZE)
    #         y = random.randint(0, SCREEN_HEIGHT-FRUIT_SIZE)
    #         temp_food_pos = pygame.Rect(x,y,FRUIT_SIZE,FRUIT_SIZE)

    #         temp_food_vs_snake = any(temp_food_pos.colliderect(seg) for seg in self.snake)

    #         temp_food_vs_sb = temp_food_pos.colliderect(self.no_tresspass)
                
    #         if not temp_food_vs_snake and not temp_food_vs_sb:
    #             self.food = temp_food_pos
    #             break

    # another more efficient way to do the same
    
    def spawn_food(self):
        # just made the transparent rect on the scoreboard just to avoid the fruit formation randomly on the scoreboard
        self.score_rect = pygame.Rect(0,0,100,100)
        
        # just created the empty list of valid positions where fruit can land safely without any interference and the safe positions will be appended here
        valid_pos = []

        # loop run over the x by width - FRUIT_SIZE with jump by FRUIT_SIZE
        for x in range(0, SCREEN_WIDTH-FRUIT_SIZE, FRUIT_SIZE):

        # loop run over the x by height - FRUIT_SIZE with jump by FRUIT_SIZE
            for y in range(0,SCREEN_WIDTH-FRUIT_SIZE, FRUIT_SIZE):

                # spaces fruit_sized are made here bcox so that if spaces collides with the seg of the snake from it's list, it means fruit can't form here, place already booked
                spaces = pygame.Rect(x,y,FRUIT_SIZE, FRUIT_SIZE)

                if any(spaces.colliderect(seg) for seg in self.snake):
                    continue
                
                # Same here if the spaces collide with the score_rect transparent box, then just continue the loop bcoz the place is already booked by the scoreboard
                if spaces.colliderect(self.score_rect):
                    continue

                # out of the if statement, if there's any avaliable space for the fruit to get assigned there, just append that space or location in the valid_pos
                valid_pos.append(spaces)

        # self.food can choose any location from valid pos
        self.food = random.choice(valid_pos)
                

    # very important method to make the game playable
    def update_pos(self, dt):

        # dx, dy are the variables where the movement is stored based on their speed and the direction of the snake
        dx, dy = 0, 0
        if self.direction == 'UP':
            dy = -SNAKE_SPEED * dt

        elif self.direction == 'DOWN':
            dy = SNAKE_SPEED * dt

        elif self.direction == 'LEFT':
            dx = -SNAKE_SPEED * dt

        elif self.direction == 'RIGHT':
            dx = SNAKE_SPEED * dt

        # if either of them is not equal to 0 then add dx and dy to rect's x and y for movement
        if dx != 0 or dy != 0:
            self.rect.x += dx
            self.rect.y += dy
            
            # commented out bcoz if not doing this, i can't make the game quit when the head collides with the walls of the surface
            # self.rect.clamp_ip(self.screen_rect)

            # insert position of head (0th index) in self.positions everytime it moves bcoz it is in if dx != 0 or dy != 0:, and the whole movement will happen just because of if dx != 0 or dy != 0:
            self.positions.insert(0, self.rect.topleft)

            # now popout the extra positions from self.positions if the len of the positions is greater than the len of self.snake times fruitsize + Gap bcoz we want to keep the gap of fruit between every chunk of the snake 

            # Better think like that the space wherever the snake moves get highlighted and if that highlighted area is more than  the required area as the fruit is eaten then pop that area, and keep the enough area, not extra
            if len(self.positions) > len(self.snake) * (FRUIT_SIZE + GAP):
                self.positions.pop()
            
            # Ran a loop on self.snake so that we can place the segment at it's required position like this one
            for i, seg in enumerate(self.snake):

                # imagine it be step variable which stores the position of every upcoming snake, and paste it down in self.positions, like for first chunk, 1 * 40(fruit_size), we has it being pasted on 40, then 80 and so on and keep the gap of 40 and paste the topleft of seg in self.positions
                step = i* (FRUIT_SIZE + GAP)
                if step < len(self.positions):
                    seg.topleft = self.positions[step]

            if self.just_ate: #if the fruit is eaten by the snake and the flag is true
                # new_seg = self.image.get_rect(topleft = self.positions[-1])
                # self.snake.append(new_seg)
                # self.just_ate = False
 
                # then tail variable hold the copy of last element of self.snake's segment and append it to the end of the snake and later put it to false, by doing this, we just make out fruit to be eaten by snake and get the size of snake increase by one chunk
                tail  = self.snake[-1].copy()
                self.snake.append(tail)
                self.just_ate = False

    # detecting the collisions
    def collision(self):

        # if snake's head hit food, score += 1, spawn food here and put the flag true
        # by doing this we get out score value increased and get the collision and food mechanics work properly
        if self.snake[0].colliderect(self.food):
            self.score += 1
            self.spawn_food()
            self.just_ate = True

        # make the game exit as the snake's head collides with any of the surface wall
        if (self.snake[0].left < 0 or self.snake[0].top < 0 or self.snake[0].right > SCREEN_WIDTH or self.snake[0].bottom > SCREEN_HEIGHT):
            sys.exit()

        # Desi method
        for seg in self.snake[4:]: #i used [4:] so that head have enough breathing space for turning bcoz as i turn, small amount of the 2nd, 3rd chunk overlaps the head and it triggers the collision and the game exit
            if self.snake[0].colliderect(seg):
                sys.exit()

    # draw method makes the whole game work
    def draw(self):
        # Screen coloring and snake blitting
        self.screen.fill(SCREEN_COLOR)

        # loop from all the seg of self.snake and then blit it on the screen
        for seg in self.snake:
            self.screen.blit(self.image, seg)
        
        # SCORE BOARD
        text = pygame.font.Font(None, 33)
        text_show = text.render(f"Score: {self.score}", True, (0,0,255))
        self.screen.blit(text_show, (20,20))

        # drawing the fruit for snake 
        pygame.draw.rect(self.screen, FRUIT_COLOR, self.food)
        pygame.display.flip()

# run the if statement if the condition is true, which means that the code is not imported from elsewhere

if __name__ == '__main__':
    sun = snake()
    sun.run()

