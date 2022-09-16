import pygame
import random

class Pipe(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 400
    
    def draw(self):
        color = (50, 105, 50)
        return pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= 2

class PipePair(object):
    def __init__(self, x):
        self.topPipe = Pipe(x, random.randrange(-350, 0))
        self.bottomPipe = Pipe(x, self.topPipe.y + 600)
    
    def draw(self):
        return [self.topPipe.draw(), self.bottomPipe.draw()]
    
    def move(self):
        global score
        self.topPipe.move()
        self.bottomPipe.move()
        if self.topPipe.x < -100:
            self.topPipe.x = 900
            self.bottomPipe.x = 900
            self.topPipe.y = random.randrange(-350, 0)
            self.bottomPipe.y = self.topPipe.y + 600
            score += 1
            print(score)

class Bird():
    def __init__(self):
        self.x = 100
        self.y = 250
    
    def draw(self):
        color = (240, 230, 140)
        pygame.draw.circle(screen, color, (self.x, self.y), 25)
    
    def move(self):
        self.y += 1


pygame.init()
screen = pygame.display.set_mode([800, 600])

# all the variables
pairs = [PipePair(900), PipePair(1250), PipePair(1600)]
bird = Bird()
cooldown = 0
gameOver = False
score = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # actual content
    screen.fill((255,255,255))
    if gameOver == False:
        for pair in pairs:
            pairData = pair.draw() #pairData = list containing the data for the top pipe and bottom pipe
            pair.move()
            for pipe in pairData: #accessing just the top pipe or just the bottom
                if pipe.collidepoint(bird.x, bird.y):
                    gameOver = True

        bird.draw()
        bird.move()

        # get Keyboard input
        key_input = pygame.key.get_pressed()
        cooldown -= 1
        if key_input[pygame.K_UP] and cooldown < 0:
            bird.y -= 60
            cooldown = 30
    
    else:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Gameover", True, (100, 255, 0), (255, 0, 0))
        textGameover = text.get_rect()
        textGameover.center = (400, 300)
        screen.blit(text, textGameover)

    

    # have everything actually become visible
    pygame.display.update()

pygame.quit()

    

