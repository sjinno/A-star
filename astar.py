import pygame
import math
from queue import PriorityQueue

SIZE = 800
WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("A* Search Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
YELLOW = (255, 255, 0)


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

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_block(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        return self.color == WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_block(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.size, self.size))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, size):
    grid = []
    gap = size // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i, j, gap, rows)
            grid[i].append(cell)
    return grid


def draw_grid(win, rows, size):
    gap = size // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (size, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, size))


def draw(win, grid, rows, size):
    win.fill(WHITE)

    for row in grid:
        for cell in row:
            cell.draw(win)

    draw_grid(win, rows, size)
    pygame.display.update()


def get_clicked_pos(pos, rows, size):
    gap = size // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, size):
    ROWS = 50
    grid = make_grid(ROWS, size)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, size)
                cell = grid[row][col]
                if not start:
                    start = cell
                    start.make_start()
                elif not end:
                    end = cell
                    end.make_end()
                elif cell != start and cell != end:
                    cell.make_block()
            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()


if __name__ == "__main__":
    main(WIN, SIZE)
