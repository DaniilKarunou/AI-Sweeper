import pygame

from static.constants import models, bombs

class Sapper():
    saper_up = pygame.image.load(f'{models}saper_up.png')
    saper_down = pygame.image.load(f'{models}saper_down.png')
    saper_left = pygame.image.load(f'{models}saper_left.png')
    saper_right = pygame.image.load(f'{models}saper_right.png')
    saper = pygame.image.load(f'{models}saper_right.png')

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.step = 60
        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )
        self.trolley= []
        self.trolley_load = 0
        self.direction = "R"

    def take_bomb(self, grid, win):
        pos = (self.x_pos, self.y_pos)
        if pos in grid.bombs.keys():
            self.trolley.append(grid.bombs.get(pos).type())
            self.trolley_load += grid.bombs.get(pos).weight
            grid.bombs.pop(pos)
        self.update_env(grid)
        win.blit(self.saper, self.saper_rect)
        pygame.display.update()

    def detonate_bomb(self, grid, win):
        pos = (self.x_pos, self.y_pos)
        if pos in grid.bombs.keys():
            grid.bombs.pop(pos)
            self.update_env(grid)
            grid.create_object(pos, "detonate.png", (60,60))
            win.blit(self.saper, self.saper_rect)
            pygame.display.update()

    def move_left(self, grid, win):
        self.saper = self.saper_left

        # odswieżanie komórek
        self.update_env(grid)

        # zmienić pozycję gracza
        if self.direction == "L":
            self.x_pos -= self.step
        else:
            self.direction = "L"
            return

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )
        win.blit(self.saper, self.saper_rect)

        # odświeżenie ekranu
        pygame.display.update()

    def move_right(self, grid, win):
        self.saper = self.saper_right

        # odswieżanie komórek
        self.update_env(grid)

        # zmienić pozycję gracza
        if self.direction == "R":
            self.x_pos += self.step

        else:
            self.direction = "R"
            return

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )
        win.blit(self.saper, self.saper_rect)

        # odświeżenie ekranu
        pygame.display.update()


    def move_up(self, grid, win):
        self.saper = self.saper_up

        # odswieżanie komórek
        self.update_env(grid)

        # zmienić pozycję gracza
        if self.direction == "U":
            self.y_pos -= self.step

        else:
            self.direction = "U"
            return

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )
        win.blit(self.saper, self.saper_rect)

        # odświeżenie ekranu
        pygame.display.update()

    def move_down(self, grid, win):
        self.saper = self.saper_down

        # odswieżanie komórek
        self.update_env(grid)

        # zmienić pozycję gracza
        if self.direction == "D":
            self.y_pos += self.step

        else:
            self.direction = "D"
            return

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )
        win.blit(self.saper, self.saper_rect)

        # odświeżenie ekranu
        pygame.display.update()

    def update_env(self, grid):
        if (self.x_pos, self.y_pos) == (0, 0):
            self.trolley.clear()
            self.trolley_load = 0

        grid.create_object((self.x_pos, self.y_pos),
                           grid.objects.get(grid.grid_matrix[self.x_pos // 60][self.y_pos // 60]),
                           (60, 60))

        if (self.x_pos, self.y_pos) in grid.bombs.keys():
            grid.create_object((self.x_pos, self.y_pos),
                               bombs[grid.bombs[(self.x_pos, self.y_pos)].type()],
                               (60, 60))

        grid.create_object((self.x_pos, self.y_pos - 60),
                                grid.objects.get(grid.grid_matrix[self.x_pos // 60][(self.y_pos - 60) // 60]),
                                (60, 60))

        if (self.x_pos, self.y_pos - 60) in grid.bombs.keys():
            grid.create_object((self.x_pos, self.y_pos - 60),
                               bombs[grid.bombs[(self.x_pos, self.y_pos - 60)].type()],
                               (60, 60))
