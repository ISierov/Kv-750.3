import random
import pygame as pg

W = 600
H = 300

COL = (0,0,128)
COL_PURPLE = (128, 0, 128)
FON_COL = (255, 204, 100)

def check_number(the_n, num_in):
    if num_in == '':
        num_in = '0'

    if the_n == int(num_in):
        res = "you are winner. Correct number is "+num_in
    elif the_n < int(num_in):
        res = "The number is less than "+num_in
    else:
        res = "The number is greater than "+num_in
    return res


pg.init()
pg.display.set_caption("moves")
gDisplay = pg.display.set_mode((W,H),pg.RESIZABLE)
font30 = pg.font.SysFont('Calibri', 25)
font40 = pg.font.SysFont('Calibri', 40)
font35 = pg.font.SysFont('Calibri', 35)

run = True
clock = pg.time.Clock()
text_in = ''
text_res = ''
attempts = 0
the_number = random.randint(1, 100)
print(the_number)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if attempts < 10:
                if event.unicode.isdigit() \
                    and (len(text_in) in [0,1] or text_in+event.unicode == '100') \
                    and not(len(text_in) == 0 and event.unicode == '0'):
                    text_in += event.unicode
                elif event.key == pg.K_BACKSPACE:
                    text_in = text_in[:-1]
                elif event.key in [pg.K_RETURN, pg.K_KP_ENTER] and text_in != '':
                    text_res = check_number(the_number, text_in)
                    attempts += 1
            else:
                text_res = "10 attempts have been exhausted"


    gDisplay.fill(FON_COL)
    gDisplay.blit(font30.render("Put your number and press ENTER:", True, COL), [5, 50])
    gDisplay.blit(font40.render(text_in, True, COL), [100,100])
    gDisplay.blit(font35.render(text_res, True, COL_PURPLE), [5, 180])
    pg.display.update()
    clock.tick(60)



