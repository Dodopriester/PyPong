import sys, pygame

pygame.init() # Initialises the behind the scene stuff

''' Declare the required variables '''
size = (320, 240)
red = (255, 0, 0)
black = 0,0,0
rectangle = pygame.Rect(20, 20, 20, 20)
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
    pygame.draw.rect(screen, red, rectangle)
    pygame.display.flip()