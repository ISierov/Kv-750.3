import pygame

###
WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500
delta = 5
coord_x = 250
coord_y = 250
COLOR = (0, 0, 216)
FON_COLOR = (255, 255, 100)
R = 10
###
pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption('Moving')

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        coord_x -= delta
        if coord_x < 0: coord_x = WIDTH_DISPLAY
    if keys[pygame.K_RIGHT]:
        coord_x += delta
        if coord_x>WIDTH_DISPLAY: coord_x = 0
    if keys[pygame.K_UP]:
        coord_y -= delta
        if coord_y < 0: coord_y = HEIGHT_DISPLAY
    if keys[pygame.K_DOWN]:
        coord_y += delta
        if coord_y > HEIGHT_DISPLAY: coord_y = 0

    gameDisplay.fill(FON_COLOR)

    pygame.draw.circle(gameDisplay, COLOR, (coord_x, coord_y), R)

    pygame.display.update()
    clock.tick(20)