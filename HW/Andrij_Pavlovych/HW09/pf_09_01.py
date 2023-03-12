import random
import pygame

FPS = 60

WIDTH_DISPLAY=800
HEIGHT_DISPLAY=500

BLACK_COLOR = (0, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()


guess_number = random.randint(1, 100)
text2 = ''

def guess(attempt):
    global text2
    if attempt > guess_number:
        text2 = f'Hidden number is less then {attempt}'
    elif attempt < guess_number:
        text2 = f'Hidden number is greater then {attempt}'
    else:
        text2 = 'You got it! Press ESC to exit'
        print_text('You got it! Press ESC to exit', 50, 380)


def print_text(message, x, y, font_color = (0, 154, 25), font_size = 20):
    font_type = pygame.font.SysFont("comicsansms", font_size)
    text = font_type.render(message, True, font_color)
    gameDisplay.blit(text, (x, y))

counter = 1

input_text = ''
while run:

    pygame.time.delay(100)

    gameDisplay.fill(BLACK_COLOR)

    print_text('Guess number from 1 to 100', 50, 20)
    print_text(f'Attempt number {counter}', 50, 50)
    print_text(f'{text2}', 50, 80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                attempt = int(input_text)
                guess(attempt)
                input_text = ''
                counter += 1
            elif event.key == pygame.K_ESCAPE:
                run = False
            else:
                input_text += event.unicode

    if counter > 10:
        print_text('You lose', 50, 180)
        run = False

    if counter < 11:
        print_text(input_text, 50, 110)

    pygame.display.update()

    clock.tick(FPS)

    

