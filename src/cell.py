from constants import *

import pygame


class Cell:
    def __init__(self, row, col, size, total_rows):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.color = WHITE
        self.neighbors = []
        self.size = size
        self.total_rows = total_rows

    def get_location(self):
        return self.row, self.col

    def is_open(self):
        return self.color == GREEN

    def is_closed(self):
        return self.color == RED

    def is_blocked(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def colorize_start(self):
        self.color = ORANGE

    def colorize_closed(self):
        self.color = RED

    def colorize_open(self):
        self.color = GREEN

    def colorize_block(self):
        self.color = BLACK

    def colorize_end(self):
        self.color = TURQUOISE

    def colorize_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.size, self.size))

    def update_neighbors(self, grid):
        self.neighbors = []
        # Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_blocked():
            self.neighbors.append(grid[self.row - 1][self.col])
        # Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_blocked():
            self.neighbors.append(grid[self.row + 1][self.col])
        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_blocked():
            self.neighbors.append(grid[self.row][self.col - 1])
        # Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_blocked():
            self.neighbors.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        return False
