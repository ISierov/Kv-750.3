import random
import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Guess a number")
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
TEXT_COL = (255, 255, 255)
FONT = pg.font.Font(None, 32)

font = pg.font.SysFont("arialblack", 20)
small_font = pg.font.SysFont("arialblack", 16)
big_font = pg.font.SysFont("arialblack", 24)
objects = []


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    # self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, TEXT_COL)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


class Button:
    def __init__(self, x, y, width, height, buttonText='Button'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (52, 78, 91))

        objects.append(self)

    def process(self):
        action = False
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed(num_buttons=3)[0] == 1 and self.alreadyPressed is False:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.alreadyPressed = True
                action = True
            if pg.mouse.get_pressed(num_buttons=3)[0] == 0:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
        return action


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def main():
    secret = random.randint(1, 100)
    entered = 0
    attempt = 1

    clock = pg.time.Clock()
    input_box = InputBox(250, 180, 100, 32)
    acc_button = Button(380, 180, 100, 32, 'Accept')
    res_button = Button(380, 230, 100, 32, 'Reset')
    done = False
    text = "Good luck!"
    nums = []

    while not done:
        screen.fill((52, 78, 91))
        acc_button.process()
        res_button.process()
        draw_text("Try  to guess a number from 1 to 100", big_font, TEXT_COL, 80, 50)

        draw_text("Your number:", font, TEXT_COL, 80, 180)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            input_box.handle_event(event)
            if res_button.process() is True:
                done = True
                main()
            if acc_button.process() is True and attempt <= 10 and entered != secret:
                entered = input_box.text
                try:
                    entered = int(entered)
                    nums.append(entered)
                except ValueError:
                    continue
                input_box.text = ''
                input_box.handle_event(event)
                if secret > entered:
                    text = "Secret number is bigger"
                elif secret < entered:
                    text = "Secret number is less"
                elif secret == entered:
                    text = f"You have guessed the correct number ({secret})!!!"
                    break
                if attempt == 10:
                    text = "You are out of attempts"
                    attempt += 1
                    break
                else:
                    attempt += 1

        draw_text(f"Attempts left: {11 - attempt}", font, TEXT_COL, 80, 120)
        draw_text(text, font, TEXT_COL, 80, 300)
        draw_text(f"Numbers entered: {str(nums)}", small_font, TEXT_COL, 80, 380)

        input_box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
