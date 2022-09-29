import sys, pygame

pygame.init() # Initialises the behind the scene stuff

''' Declare the required variables '''
size = (320, 240)
red = (255, 0, 0)
black = 0,0,0
player1 = pygame.Surface((20,80))
player2 = pygame.Surface((20,80))

player1.fill((255,255,255))
player2.fill((255,255,255))

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

    pygame.display.flip()