import os
import pygame as pg
from random import choice, randrange

class Symbol:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.value = choice(green_letters)
        self.interval = randrange(20, 40)

    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_letters if color == 'green' else lightgreen_letters)

        self.x = self.x + self.speed if self.x < WIDTH else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))



class SymbolColumn:
    def __init__(self, x, y):
        self.column_width = randrange(8, 24)
        self.speed = randrange(1, 3)
        self.symbols = [Symbol(y, i, self.speed) for i in range(x, x - FONT_SIZE * self.column_width, -FONT_SIZE)]
        self.column_interval = randrange(10, 20)

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]



os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 40
alpha_value = 0

pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
clock = pg.time.Clock()


letters = ["крысы", "листовки", "белый ферзь", "черная королева", "шахматы", "zomaro", "razoom", "вместе"]
# letters = [chr(int('0x30A0', 16) + i) for i in range(96)]
# letters = ["a", "b", "c", "d", "e", "f"]
font = pg.font.Font('arial', FONT_SIZE)
green_letters = [font.render(char, True, (40, randrange(160, 256), 40)) for char in letters]
lightgreen_letters = [font.render(char, True, pg.Color('lightgreen')) for char in letters]

symbol_columns = [SymbolColumn(y, randrange(-HEIGHT, 0)) for y in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    if not pg.time.get_ticks() % 20 and alpha_value < 170:
        alpha_value += 6
        surface.set_alpha(alpha_value)

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)
