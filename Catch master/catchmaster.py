import pygame
import random
import os
pygame.init()

# making a window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 400

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch Master')

# background
backgroundHeight = SCREEN_HEIGHT
backgroundWidth = SCREEN_WIDTH*2
backgroundX = 0
backgroundY = 0
backgroundVelocity = 0.25
backgroundImage = pygame.image.load("Assets/background.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (backgroundWidth, backgroundHeight))
backgroundImage2 = backgroundImage



class Apple(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((objectWidth, objectHeight))
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    # object movement + collision
    def update(self):
        self.rect.move_ip(0,5)
        if y < self.rect.bottom < (y+playerHeight) and x-(objectWidth/2) < self.rect.centerx < (x+playerWidth)+objectWidth/2:
            self.kill()
            global score
            score += 1
            object = Apple(appleSprite, random.randint(10, SCREEN_WIDTH-objectWidth-10), random.randint(-SCREEN_HEIGHT, -25))
            objects.add(object)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

            


# player
playerHeight = 20
playerWidth = 80
x = (SCREEN_HEIGHT - playerWidth) / 2
y = SCREEN_HEIGHT - playerHeight - 50
playerVelocity = 7.5

basketSprite = pygame.image.load("Assets/basket.png").convert_alpha()
basketSprite = pygame.transform.scale(basketSprite, (playerWidth, playerHeight))

# falling objects
objectWidth = 24
objectHeight = 24
objectVelocity = 5
# object sprites
appleSprite = pygame.image.load("Assets/apple.png").convert_alpha()
appleSprite = pygame.transform.scale(appleSprite, (objectWidth, objectHeight))

objects = pygame.sprite.Group()
for i in range(5):
    object = Apple(appleSprite, random.randint(10, SCREEN_WIDTH-objectWidth-10), random.randint(-SCREEN_HEIGHT, -25))
    objects.add(object)
    

# game
score = 0
myfont = pygame.font.SysFont("sans serif", 50)

# power ups
cooldown = 0





FPS = 60
# main loop
run = True
while run:
    # fps
    pygame.time.delay(int(1000/FPS))
    # checks for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > playerVelocity:
        x -= playerVelocity
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - playerWidth - playerVelocity:
        x += playerVelocity

    # power ups
    if cooldown > 0:
        cooldown -= 1/FPS
    if keys[pygame.K_f] and cooldown <= 0:
        cooldown = 10
        for i in range(5):
            object = Apple(appleSprite, random.randint(10, SCREEN_WIDTH-objectWidth-10), random.randint(-SCREEN_HEIGHT, -25))
            objects.add(object)
            print('sprite added')

    
    # move background
    if backgroundX <= -backgroundWidth:
        backgroundX += backgroundWidth
    else:
        backgroundX -= backgroundVelocity

    # if no more objects
    if not objects.sprites():
        gameEnd()
        continue

    # background
    win.blit(backgroundImage, (backgroundX, backgroundY))
    win.blit(backgroundImage2, (backgroundX+backgroundWidth, backgroundY))

    # objects
    objects.update()
    objects.draw(win)
    # player
    win.blit(basketSprite, (x, y))
    # score
    scoreText = myfont.render(f'Score: {score}', 1, (0,0,0))
    win.blit(scoreText, (20, 20))
    pygame.display.update()

    def gameEnd():
        # background
        win.blit(backgroundImage, (backgroundX, backgroundY))
        win.blit(backgroundImage2, (backgroundX+backgroundWidth, backgroundY))

        # game over text
        gameOverText = myfont.render('Game Over!', 1, (0,0,0))
        win.blit(gameOverText, ((SCREEN_WIDTH-gameOverText.get_width())/2, (SCREEN_HEIGHT-gameOverText.get_height())/2))
        # score
        scoreText = myfont.render(f'Score: {score}', 1, (0,0,0))
        win.blit(scoreText, (20, 20))
        pygame.display.update()







pygame.QUIT