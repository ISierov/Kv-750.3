import pygame
import random


pygame.init() 

clock = pygame.time.Clock()

disp_size = (1000,600)

# Display
GameDisplay = pygame.display.set_mode(disp_size, pygame.RESIZABLE)
pygame.display.set_caption('???  number guesser  ???')


# text_func
text_font = pygame.font.Font(None, 60)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    GameDisplay.blit(img, (x, y))

input_texr = ''

# main loop
ges_num = random.randint(1,100)
attempts = 1
feedback = ''
win_control = False

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:   #bind BACKSPACE
                input_texr = input_texr[:-1]
            elif event.key == pygame.K_SPACE:      #input number
                
                NUM = input_texr
                    
                if win_control :                               #main func
                    feedback ='та все :) , ти вже виграв'

                elif NUM.isdigit() and attempts <= 10:
                    attempts += 1
                    if int(NUM) == ges_num :
                        feedback = 'ТИ ВИГРАВ !!!!!'
                        win_control = True
                    elif int(NUM) > ges_num :
                        feedback ='спробуй менше число'
                            
                    elif int(NUM) < ges_num :
                        feedback ='спробуй більше число'
                elif attempts <= 10 :
                    feedback ='щось не те ти написав'
                    attempts += 1
                else:
                    feedback ='спроби вичерпано'

                input_texr = ''

            else:
                input_texr += event.unicode    
            
           

    GameDisplay.fill((40,150,130))

    draw_text('Зможеш відгадати число від 1 до 100 ?', text_font, (0,0,0), 80,100)
    draw_text('в тебе 10 спроб (друкуй та тисни "spase")', text_font, (0,0,0), 60,150)
    draw_text(input_texr, text_font, (100,10,30), 450,250)
 
    draw_text(feedback, text_font, (0,0,0), 300,400)

    pygame.display.update()
