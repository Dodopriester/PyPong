import sys, pygame
from random import randint

pygame.init() # Initialises the behind the scene stuff

''' Declare the required variables '''
size = (320, 240)
red = (255, 0, 0)
black = 0,0,0
player1 = pygame.Surface((20,80))
player2 = pygame.Surface((20,80))
ball = pygame.Surface((20,20))

player1.fill((255,255,255))
player2.fill((255,255,255))
ball.fill((255,0,0))

posx = 100
posy = 50
speed = [1, 1]

playerpos1 = [20, 50]
playerpos2 = [280, 50]

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
key_pressed = False

''' Start the update loop '''
while True:
    clock.tick(60)

    ''' Listen to events '''
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()

    screen.fill(black)

    screen.blit(player1, playerpos1)
    screen.blit(player2, playerpos2)
    posx += speed[0]
    posy += speed[1]

    if(posx > 300):
        speed[0] = -abs(speed[0])
    elif(posx < 0):
        speed[0] = abs(speed[0])

    if(posy < 0):
        speed[1] = abs(speed[1])
    elif(posy > 220):
        speed[1] = -abs(speed[1])

    if (playerpos1[0] < posx + 20 and
    playerpos1[0] + 20 > posx and
    playerpos1[1] < posy + 20 and
    playerpos1[1] + 80 > posy):
        speed[0] *= -1
        speed[1] = randint(-4,4)

    if (playerpos2[0] < posx + 20 and
    playerpos2[0] + 20 > posx and
    playerpos2[1] < posy + 20 and
    playerpos2[1] + 80 > posy):
        speed[0] *= -1
        speed[1] = randint(-4,4)

    screen.blit(ball, (posx, posy))

    pygame.display.flip()

