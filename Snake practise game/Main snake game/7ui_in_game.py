import pygame
import sys
import random
import json

pygame.init()
pygame.mixer.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH  = 1200

SNAKE_SIZE = 60
FRUIT_SIZE = 60 

SCREEN_COLOR = (0,255,0)

SPEED_RISE = 1.01

pause_pos = SCREEN_WIDTH - 70

class Snake:
    def __init__(self):

        # screen_settings
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Professional snake game')
        self.screen_rect = self.screen.get_rect()

        # snake_settings
        self.normal_image = pygame.image.load('IMAGES/3.jpg')
        self.image = pygame.transform.scale(self.normal_image, (SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.image.get_rect()
        self.speed = 1

        # FLAGS
        self.fruit_on_snake = False
        self.snake_hit = False
        self.just_ate = False

        # CLOCK
        self.clock = pygame.time.Clock()

        # LIST
        self.snake = [self.rect]
        self.positions = [self.rect.topleft]

        # direction
        self.direction = 'UP'

        # SPAWN FOOD
        self.spawn_food()

        # positioning
        self.rect.midbottom = self.screen_rect.midbottom

        # Game pause or start method
        self.game_pause = False
        self.game_running = True
        self.snake_died_sound = False

        # scoring
        self.score = 1
        self.highscore = self.load_data()
        
        # sounds
        self.eat_sound = pygame.mixer.Sound("./Sound/food-ate.mp3")
        self.game_lose = pygame.mixer.Sound("./Sound/game-over.mp3")
        self.game_start = pygame.mixer.Sound("./Sound/game-start.mp3")
        self.click = pygame.mixer.Sound("./Sound/select.mp3")
        pygame.mixer.music.load("./Sound/snowfall.mp3")
        pygame.mixer.music.play(-1)

    def Run(self):
        # dt = self.clock.tick(60)/1000
        while True:
            self.Events()
            if self.snake_hit or self.game_pause:
                if self.snake_hit:
                    self.snakecolliderects()

                elif self.game_pause:
                    self.popup_ui()

            else:
                self.Update_Pos()

            self.collision()
            self.draw()

    def save_data(self):
        hscore_data = {"High Score": self.highscore}
        with open('data.json', "w") as h_file:
            json.dump(hscore_data, h_file, indent=4)
    
    def load_data(self):
        try:
            with open('data.json', 'r') as h_file:
                h_score = json.load(h_file)
                return h_score.get("High Score", 1)
        except FileNotFoundError:
            return 1

    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            
            elif event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.pausebutton_rect.collidepoint(event.pos):
                        self.click.play()
                        self.game_pause = True
                    if self.game_pause:
                        if self.resumebutton_rect.collidepoint(event.pos):
                            self.click.play()
                            self.game_pause = False

                        if self.quitbutton_rect.collidepoint(event.pos):
                            self.click.play()
                            pygame.quit()
                            sys.exit()
                        if self.restartbutton_rect.collidepoint(event.pos):
                            self.click.play()
                            self.restart_game()

                    if self.snake_hit:

                        self.game_pause = False
                        
                        if self.hitquitbg.collidepoint(event.pos):
                            
                            pygame.quit()
                            sys.exit()
                        
                        if self.hitrestartbg.collidepoint(event.pos):
                            self.click.play()
                            self.restart_game()
                            self.snake_hit = False
                        

    def _keydown_events(self, event):
    
        if event.key == pygame.K_p and not self.snake_hit:
            self.game_pause = True
            self.click.play()

        elif event.key == pygame.K_a and (self.game_pause or self.snake_hit):
            self.game_pause = False
            self.snake_hit = False
            self.restart_game()
            self.click.play()
        
        elif event.key == pygame.K_r and self.game_pause:
            self.game_pause = False
            self.click.play()

        elif event.key == pygame.K_q:
            self.click.play()
            pygame.quit()
            sys.exit()

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
        

    def spawn_food(self):
        # Making score_board getting saved from food being spawned on it
        self.score_rect = pygame.Rect(0,0,200,100)
        self.highscore_rect = pygame.Rect(0,100,200,100)

        self.pausebutton_rect = pygame.Rect(pause_pos, 0,50,50)
        
        avaliable_space = []

        for x in range(0, SCREEN_WIDTH , FRUIT_SIZE):
            for y in range(0, SCREEN_HEIGHT, FRUIT_SIZE):
                Fruit_rect = pygame.Rect(x,y,FRUIT_SIZE,FRUIT_SIZE)
                
                if Fruit_rect.colliderect(self.score_rect) or Fruit_rect.colliderect(self.highscore_rect):
                    continue

                if any(Fruit_rect.colliderect(seg) for seg in self.snake):
                    continue

                if Fruit_rect.colliderect(self.pausebutton_rect):
                    continue

                avaliable_space.append(Fruit_rect)
        if avaliable_space:
            self.food = random.choice(avaliable_space)
        else:
            self.snake_hit = True

    def Update_Pos(self):
        dx, dy = 0,0 
        if self.direction == 'UP':
            dy = -self.speed 
        elif self.direction == 'DOWN':
            dy = self.speed 
        elif self.direction == 'LEFT':
            dx = -self.speed 
        elif self.direction == 'RIGHT':
            dx = self.speed 

        if dx != 0 or dy != 0:
            self.rect.x += dx
            self.rect.y += dy

            # inserting the positions of the rect's topleft corner to the self.positions list in 0th index because whenever new segment will be added, it will take the previous position to that of head's current position

            self.positions.insert(0, self.rect.topleft)

            if len(self.positions) > len(self.snake) * SNAKE_SIZE:
                self.positions.pop()

            # following the head
            for i, seg in enumerate(self.snake):
                step = i * SNAKE_SIZE
                if step < len(self.positions):
                    seg.topleft = self.positions[step]

            if self.just_ate: 
                tail_pos = self.snake[-1].copy()
                self.snake.append(tail_pos)

                self.just_ate = False

    def button_rects(self):
        self.restartbutton_rect = pygame.Rect(450,200,200,40)

        self.resumebutton_rect = pygame.Rect(450,250,200,40)

        self.quitbutton_rect = pygame.Rect(450,300,200,40)

    def button_ui(self):
        self.text_pause = pygame.font.Font(None, 53)
        self.text_pause.set_bold(True)
        pause_button = self.text_pause.render("||", True, (0,0,255))
        self.screen.blit(pause_button, (pause_pos, 10))

    def popup_ui(self):
        # Start button
        self.restart = pygame.font.Font(None,40)
        self.button_rects()
        pygame.draw.rect(self.screen, (217,171,72), self.restartbutton_rect)
        restart_button = self.restart.render("Restart", True, (255,255,255))
        self.screen.blit(restart_button,(500,208))

        # resume button 
        self.resume = pygame.font.Font(None, 40)
        resume_button = self.resume.render("Resume", True, (255,255,255))
        pygame.draw.rect(self.screen, (217,171,72), self.resumebutton_rect)
        self.screen.blit(resume_button, (500, 258))

        # Quit button
        self.quit = pygame.font.Font(None, 40)
        quit_button = self.resume.render("Quit", True, (255,255,255))
        pygame.draw.rect(self.screen, (217,171,72), self.quitbutton_rect)
        self.screen.blit(quit_button, (500,308))
    
    def restart_game(self):
        self.score = 1
        self.snake = [self.rect]
        while len(self.snake) > 1:
            self.snake.pop()
        self.positions = [self.rect.topleft]
        while len(self.positions) > 1:
            self.positions.pop()
        self.direction = 'UP'
        self.rect.midbottom = self.screen_rect.midbottom
        self.game_pause = False
        self.snake_hit = False
        self.snake_died_sound = False
        self.game_start.play()
        self.spawn_food()

    def snakecolliderects(self):
        self.main_box = pygame.Rect(420,170,300,150)
        
        pygame.draw.rect(self.screen, (48,71,67), self.main_box)

        self.score_onmain = pygame.font.Font(None, 33)
        self.highscore_onmain = pygame.font.Font(None, 33)

        self.score_board = self.score_onmain.render(f"Score: {self.score}", True, (255,255,255))
        self.highscore_board = self.highscore_onmain.render(f"H. Score: {self.highscore}", True, (255,255,255))

        self.restart_onmain = pygame.font.Font(None,33)
        self.quit_onmain = pygame.font.Font(None, 33)

        self.hitrestartbg = pygame.Rect(435,237,100,50)
        pygame.draw.rect(self.screen, (98,117,167), self.hitrestartbg)
        self.hitrestartbutton = self.restart_onmain.render("Restart", True, (255,255,255))

        self.hitquitbg = pygame.Rect(600,237,100,50)
        pygame.draw.rect(self.screen, (98,117,167), self.hitquitbg)
        self.hitquitbutton = self.quit_onmain.render("Quit", True, (255,255,255))

        self.screen.blit(self.score_board, (440,200))
        self.screen.blit(self.highscore_board, (590,200))
        self.screen.blit(self.hitrestartbutton, (450,250))
        self.screen.blit(self.hitquitbutton, (630,250))
                    
    def collision(self):
        if self.snake[0].colliderect(self.food):
            self.eat_sound.play()
            self.score +=1
            if self.score > self.highscore:
                self.highscore = self.score
                self.save_data()

            # min() is the way to limit the speed of snake going beyond control, first argument will let the speed rise freely until it is less than 2nd argument, once it cross the 2nd one, the speed will be clamped at 20, no matter how high the value of self.speed * SPEED_RISE is, it makes the game playable at high levels
            self.speed = min(self.speed * SPEED_RISE, 20)
            self.spawn_food()
            self.just_ate = True

        if (self.snake[0].top < 0 or self.snake[0].left < 0 or self.snake[0].right >= SCREEN_WIDTH or self.snake[0].bottom >= SCREEN_HEIGHT) :
            self.snake_hit = True
            if not self.snake_died_sound:
                self.game_lose.play()
                self.snake_died_sound = True

        snake_col_copy = self.snake[4:]
        for seg in snake_col_copy:
            if self.snake[0].colliderect(seg):
                self.snake_hit = True
                if not self.snake_died_sound:
                    self.game_lose.play()
                    self.snake_died_sound = True
                self.snakecolliderects()
    
    def draw(self):
        self.screen.fill(SCREEN_COLOR)
        pygame.draw.rect(self.screen, (255,0,0), self.food)
        for seg in self.snake:
            self.screen.blit(self.image, seg)

        self.button_ui()
        if self.game_pause:
            self.bg_of_popup = pygame.Rect(420,170,260,200)
            pygame.draw.rect(self.screen, (48,71,67), self.bg_of_popup)
            self.popup_ui()

        if self.snake_hit:
            self.snakecolliderects()

        text = pygame.font.Font(None, 40)
        font = text.render(f"Score: {self.score}", True, (0,0,255))
        highfont = text.render(f"H.Score: {self.highscore}", True, (0,0,255))
        self.screen.blit(font, (20,20))
        self.screen.blit(highfont, (20,50))

        pygame.display.flip()

if __name__ == '__main__':
    snake = Snake()
    snake.Run()
            
