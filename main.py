import sys, pygame

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

posx = 0
posy = 0
speed = [1,1]

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

''' Start the update loop '''
while True:
    clock.tick(60)

    ''' Listen to events '''
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()
    
    screen.fill(black)

    screen.blit(player1, (20,50))
    screen.blit(player2, (280,50))
    posx += speed[0]
    posy += speed[1]

    if(posx > 300):
        speed[0] = -1
    elif(posx < 0):
        speed[0] = 1

    if(posy < 0):
        speed[1] = 1
    elif (posy > 220):
        speed[1] = -1


    screen.blit(ball, (posx, posy))

    pygame.display.flip()