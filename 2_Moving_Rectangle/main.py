import sys, pygame

pygame.init() # Initialises the behind the scene stuff

''' Declare the required variables '''
size = (320, 240)
red = (255, 0, 0)
black = 0,0,0
rectangle = pygame.Rect(20, 20, 20, 20)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = [0.1, 0.1]

''' Start the update loop '''
while True:
    dt = clock.tick(60)

    ''' Listen to events '''
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()

    screen.fill(black)   
    rectangle.move_ip(dt * speed[0], dt * speed[1]) # Move the rectangle in the direction of the speed variable

    # How can we implement collision detection?

    pygame.draw.rect(screen, red, rectangle) 
    pygame.display.flip()

    