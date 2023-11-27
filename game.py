import threading
import pygame
from gameObjects.Saper import Sapper
from gameObjects.elems import Duzykamien
from gameObjects.grid import Grid
from connectAItoGame import ConnectAItoGame

class Game():
    def __init__(self, grid_size):
        pygame.init()
        self.win = pygame.display.set_mode((grid_size[0]*60, grid_size[1]*60))
        pygame.display.set_caption("Saper")
        self.run = True
        self.clock = pygame.time.Clock()
        self.grid = Grid(grid_size, self.win)
        self.saper = Sapper()
        self.win.blit(self.saper.saper, self.saper.saper_rect)
        pygame.display.update()
        self.Agent = ConnectAItoGame(self.grid.grid_matrix)
        self.x = threading.Thread(target=self.Agent.completeGame, args=(self.saper, self.grid, self.win,))
        self.x.start()

    def start_game(self):
        while self.run:
            # opóźnienie w grze
            pygame.time.delay(10)
            self.clock.tick(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # obsługa zdarzeń
            keys = pygame.key.get_pressed()

            if (self.saper.x_pos == 0) and (self.saper.y_pos == 0):
                self.saper.trolley.clear()
                self.saper.trolley_load = 0

            if keys[pygame.K_LEFT] and (self.saper.x_pos - self.saper.step > -60 or self.saper.direction != "L") \
                    and (self.grid.grid_matrix[(self.saper.x_pos - self.saper.step)//60][self.saper.y_pos//60] != Duzykamien().koszt
                    or self.saper.direction != "L"):
                self.saper.move_left(self.grid, self.win)


            if keys[pygame.K_RIGHT] and (self.saper.x_pos + self.saper.step < self.win.get_width() or self.saper.direction != "R") \
                    and (self.grid.grid_matrix[(self.saper.x_pos + self.saper.step)//60][self.saper.y_pos//60] != Duzykamien().koszt
                    or self.saper.direction != "R"):
                self.saper.move_right(self.grid, self.win)


            if keys[pygame.K_UP] and (self.saper.y_pos - self.saper.step > -60 or self.saper.direction != "U") \
                    and (self.grid.grid_matrix[self.saper.x_pos//60][(self.saper.y_pos - self.saper.step)//60] != Duzykamien().koszt
                    or self.saper.direction != "U"):
                self.saper.move_up(self.grid, self.win)

            if keys[pygame.K_DOWN] and (self.saper.y_pos + self.saper.step < self.win.get_height() or self.saper.direction != "D") \
                    and (self.grid.grid_matrix[self.saper.x_pos//60][(self.saper.y_pos + self.saper.step)//60] != Duzykamien().koszt
                    or self.saper.direction != "D"):
                self.saper.move_down(self.grid, self.win)

            if keys[pygame.K_k]:
                self.saper.take_bomb(self.grid, self.win)

            if keys[pygame.K_d]:
                self.saper.detonate_bomb(self.grid, self.win)

            if not self.grid.bombs and not self.saper.trolley:
                self.run = False
                self.grid.create_object((0,0), "win.jpg", (540, 540))



