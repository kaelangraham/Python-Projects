import pygame
import random
pygame.init()

# making a window
screenHeight = 600
screenWidth = 400

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Catch Master')

# player
playerHeight = 10
playerWidth = 80
x = (screenHeight - playerWidth) / 2
y = screenHeight - playerHeight - 50
playerVelocity = 7.5

# falling objects
objectWidth = 20
objectHeight = 20
objectVelocity = 5
objects = []
for i in range(5):
    objects.append([random.randint(10, screenWidth-objectWidth-10),random.randint(-screenHeight, -25)])

    

# game
score = 0
myfont = pygame.font.SysFont("sans serif", 50)


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
    if keys[pygame.K_RIGHT] and x < screenWidth - playerWidth - playerVelocity:
        x += playerVelocity

    # object movement + collision
    tempList = []
    for  obj in objects:
        objx = obj[0]
        objy = obj[1]

        # if collided with player
        if y <= (objy+objectHeight) <= (y+playerHeight) and (x-objectWidth) <= objx <= (x+playerWidth):
            score += 1
            tempList.append([random.randint(10, screenWidth-objectWidth-10),random.randint(-screenHeight, -25)])
        elif objy >= screenHeight:
            tempList.append([random.randint(10, screenWidth-objectWidth-10),random.randint(-screenHeight, -25)])
        else:
            obj[1] += objectVelocity
            tempList.append(obj)
    
    objects = tempList
        
    # draw display
    win.fill((0,0,0))
    # objects
    for obj in objects:
        pygame.draw.rect(win, (255,255,255), (obj[0],obj[1],objectWidth,objectHeight))
    # player
    pygame.draw.rect(win, (255,0,0), (x,y,playerWidth,playerHeight))
    # score
    scoreText = myfont.render(f'Score: {score}', 1, (255,255,255))
    win.blit(scoreText, (20, 20))
    pygame.display.update()


pygame.QUIT