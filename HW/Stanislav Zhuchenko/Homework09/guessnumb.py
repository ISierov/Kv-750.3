import pygame
from random import randrange

pygame.init()
pygame.font.init()

FON_COLOR = (128, 128, 0)
FON_RECT_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)

FONT = pygame.font.Font(None, 30)  # initialized font and font size for label
FONT_INPUT = pygame.font.Font(None, 50)  # initialized font and font size for input text

WIDTH_DISPLAY = 950
HEIGHT_DISPLAY = 500
WIDTH_RECT1 = 75
HEIGHT_RECT1 = 75
WIDTH_RECT2 = 800
HEIGHT_RECT2 = 75

number = randrange(0, 100, 1)

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption('Guess the number')

KEYS_NUMBER = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
               pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

run = True
user_text = ''
history_text = ''
counter = 10
res = 0
hint = None

while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key in KEYS_NUMBER:
                user_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[0:-1]
            elif event.key == pygame.K_RETURN:

                try:
                    if number == int(user_text):
                        res = 1
                        history_text += f'[{user_text}]'
                        user_text = ''
                        counter -= 1
                    else:
                        if number < int(user_text):
                            hint = 'The guess number is less'
                        elif number > int(user_text):
                            hint = 'The guess number is more'
                        counter -= 1

                        if counter == 0:
                            history_text += user_text
                            user_text = ''
                        else:
                            history_text += user_text + ', '
                            user_text = ''
                except ValueError:
                    hint = 'Enter numbers only'

        gameDisplay.fill(FON_COLOR)

        label = FONT_INPUT.render('Guess the number from 0 to 100 in 10 attempt', True, FONT_COLOR)
        gameDisplay.blit(label, (120, 5))

        input_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (75, 75, WIDTH_RECT1, HEIGHT_RECT1))
        input_label = FONT.render('Input', True, FONT_COLOR)  # render a text, with antialias and FONT_COLOR
        gameDisplay.blit(input_label, (85, 50))  # display text on gameDisplay
        input_text = FONT_INPUT.render(user_text, True, FONT_COLOR)
        gameDisplay.blit(input_text, (input_rect.x + 5, input_rect.y + 20))

        history_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (75, 225, WIDTH_RECT2, HEIGHT_RECT2))
        history_label = FONT.render('History', True, FONT_COLOR)
        gameDisplay.blit(history_label, (85, 200))
        input_history = FONT_INPUT.render(history_text, True, FONT_COLOR)
        gameDisplay.blit(input_history, (history_rect.x + 5, history_rect.y + 20))

        # Add counter that count our input
        counter_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (450, 75, WIDTH_RECT1, HEIGHT_RECT1))
        counter_label = FONT.render('Counter', True, FONT_COLOR)
        gameDisplay.blit(counter_label, (450, 50))
        count_text = FONT_INPUT.render(str(counter), True, FONT_COLOR)
        gameDisplay.blit(count_text, (475, 100))

        message = FONT_INPUT.render(hint, True, FONT_COLOR)
        gameDisplay.blit(message, (250, 350))
        pygame.display.flip()

        if res == 1 and counter >= 0:
            hint = 'You WIN!!'

            input_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (75, 75, WIDTH_RECT1, HEIGHT_RECT1))

            counter_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (450, 75, WIDTH_RECT1, HEIGHT_RECT1))
            count_text = FONT_INPUT.render(str(counter), True, FONT_COLOR)
            gameDisplay.blit(count_text, (475, 100))

            input_history = FONT_INPUT.render(history_text, True, FONT_COLOR)
            gameDisplay.blit(input_history, (history_rect.x + 5, history_rect.y + 20))

            pygame.display.update()

        elif res != 1 and counter == 0:
            hint = 'Try again!!!'

            input_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (75, 75, WIDTH_RECT1, HEIGHT_RECT1))

            counter_rect = pygame.draw.rect(gameDisplay, FON_RECT_COLOR, (450, 75, WIDTH_RECT1, HEIGHT_RECT1))
            count_text = FONT_INPUT.render(str(counter), True, FONT_COLOR)
            gameDisplay.blit(count_text, (475, 100))

            input_history = FONT_INPUT.render(history_text, True, FONT_COLOR)
            gameDisplay.blit(input_history, (history_rect.x + 5, history_rect.y + 20))

            pygame.display.update()
