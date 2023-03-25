import pygame

FPS = 60

WIDTH_DISPLAY = 800
HEIGHT_DISPLAY = 600

COORD_X = 20
COORD_Y = 20
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 35

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if COORD_X >= 15:
            COORD_X = COORD_X - DELTA_STEP
        else:
            COORD_X = 0
    if keys[pygame.K_RIGHT]:

        if COORD_X < gameDisplay.get_width() - (WIDTH_RECTANGLE+DELTA_STEP):
            COORD_X = COORD_X + DELTA_STEP
        else:
            COORD_X = gameDisplay.get_width()-WIDTH_RECTANGLE
    if keys[pygame.K_UP]:
        if COORD_Y >= 15:
            COORD_Y = COORD_Y - DELTA_STEP
        else:
            COORD_Y = 0
    if keys[pygame.K_DOWN]:
        if COORD_Y < gameDisplay.get_height() - (HEIGHT_RECTANGLE+DELTA_STEP):
            COORD_Y = COORD_Y + DELTA_STEP
        else:
            COORD_Y = gameDisplay.get_height() - HEIGHT_RECTANGLE

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
