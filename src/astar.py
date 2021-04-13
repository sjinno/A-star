import math
from queue import PriorityQueue

from cell import Cell
from constants import *

import pygame


WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("A* Search Algorithm")


# Heuristic function that estimates a rough distance
# between `current` position and `end` position.
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.colorize_path()
        draw()


# A* search algorithm
def astar_search(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {cell: float('inf') for row in grid for cell in row}
    g_score[start] = 0

    f_score = {cell: float('inf') for row in grid for cell in row}
    f_score[start] = h(start.get_location(), end.get_location())

    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            start.colorize_start()
            end.colorize_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_location(), end.get_location())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.colorize_open()

        draw()

        if current != start:
            current.colorize_closed()

    return False


def make_grids(rows, size):
    grids = []
    gap = size // rows
    for i in range(rows):
        grids.append([])
        for j in range(rows):
            cell = Cell(i, j, gap, rows)
            grids[i].append(cell)
    return grids


def draw_grids(win, rows, size):
    gap = size // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (size, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, size))


def draw(win, grids, rows, size):
    win.fill(WHITE)
    for row in grids:
        for cell in row:
            cell.draw(win)
    draw_grids(win, rows, size)
    pygame.display.update()


def get_clicked_pos(pos, rows, size):
    gap = size // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col
