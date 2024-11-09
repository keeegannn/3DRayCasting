import pygame as pg
from settings import *
from raycasting import *
from map import *
from player import *
import sys

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.map = Map(self)
        self.ray_caster = RayCasting(self)

    def update(self):
        self.player.update()
        self.ray_caster.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        # self.player.draw()
        # self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.KEYUP):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()