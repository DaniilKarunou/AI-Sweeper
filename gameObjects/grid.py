import random
import pygame
from static.constants import grass, rock, big_rock, water, walls, models, temp, bombs, \
    bomb_to_int
from gameObjects.bombs import Mine, Grenade, WaterMine, AirBomb, C4, FakeBomb, HandBomb, Molotov, NukeBomb, TNT
from gameObjects.elems import Duzykamien, Kaluza, Rock, Grass
from gameTools.tools import resize_image

class Grid():

    def __init__(self, size, window):
        self.objects = {1: grass,
                        2: rock,
                        5: big_rock,
                        4: water}
        self.window = window
        self.grid_matrix = []
        self.size = size
        self.SCREEN_HEIGHT = window.get_height()
        self.SCREEN_WIDTH = window.get_width()
        self.TILE_SIZE = (60, 60)
        self.BOMBS_NUM = size[0] - 1
        self.bombs = {}
        self.create_grid(self.size)
        self.spawn_bombs()
        pygame.display.update()


    #powstanie macierzy z wylosowanymi nazwami objektów, a potem rysowanie kratki na podstawie tej macierzy
    def create_grid(self, size):
        matrix = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                if (i, j) in walls:
                    row.append(Duzykamien().koszt)
                else:
                    row.append(random.choice((Kaluza().koszt, Rock().koszt, Grass().koszt)))
            matrix.append(row)

        self.grid_matrix = matrix
        self.draw_grid(matrix)

    def draw_grid(self, grid_matrix):
        # rysowanie wierszy
        for i in range(len(grid_matrix)):
            # rysowanie kolumn
            for j in range(len(grid_matrix[0])):
                self.create_object((i * 60, j * 60), self.objects.get(grid_matrix[i][j]), (60, 60))

    def spawn_bombs(self):
        counter = 0
        while counter != self.BOMBS_NUM:
            x = int(random.randrange(0, self.SCREEN_HEIGHT-60, 60))
            y = int(random.randrange(0, self.SCREEN_WIDTH-60, 60))
            bomb_pos = (x, y)
            bomb = random.choice([Mine((x, y)), Grenade((x, y)), WaterMine((x, y)), WaterMine((x, y)), AirBomb((x, y)), C4((x, y)),
                                  FakeBomb((x, y)), HandBomb((x, y)), Molotov((x, y)), NukeBomb((x, y)), TNT((x, y))])

            if (bomb_pos not in self.bombs.keys()) and (bomb_pos != (0, 0)) and (self.grid_matrix[x//60][y//60] == bomb_to_int[bomb.place_ground]):
                self.bombs[bomb_pos] = bomb
                self.create_object(bomb_pos, bombs[bomb.type()], self.TILE_SIZE)
                counter += 1

    #funkcja rysowania objektów
    def create_object(self, position, object_name, object_size):
        self.window.blit(resize_image(f"{models}{object_name}", f"{temp}{object_name}", object_size), position)
