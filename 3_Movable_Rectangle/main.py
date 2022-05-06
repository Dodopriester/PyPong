import sys, pygame

pygame.init()  # Initialises the behind the scene stuff

''' Declare the required variables '''
size = (320, 240)
color = (255, 255, 255)
black = 0, 0, 0
rectangle = pygame.Rect(20, 20, 20, 50)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = [0.1, 0.1]

pygame.key.set_repeat(10)

''' Start the update loop '''
while True:
    dt = clock.tick(60)

    ''' Listen to events '''
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            rectangle.move_ip(0, -dt * 0.2)
        if keys_pressed[pygame.K_DOWN]:
            rectangle.move_ip(0, dt * 0.2)

    screen.fill(black)
#    rectangle.move_ip(dt * speed[0], dt * speed[1])  # Move the rectangle in the direction of the speed variable

    pygame.draw.rect(screen, color, rectangle)
    pygame.display.flip()