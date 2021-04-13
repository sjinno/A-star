from astar import *
from constants import ROWS


def main(win, size):
    grids = make_grids(ROWS, size)
    start = None
    end = None
    run = True

    while run:
        draw(win, grids, ROWS, size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Left click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, size)
                cell = grids[row][col]
                if not start and cell != end:
                    start = cell
                    start.colorize_start()
                elif not end and cell != start:
                    end = cell
                    end.colorize_end()
                elif cell != start and cell != end:
                    cell.colorize_block()
            # Right click
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, size)
                cell = grids[row][col]
                cell.reset()
                if cell == start:
                    start = None
                elif cell == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grids:
                        for cell in row:
                            cell.update_neighbors(grids)

                    astar_search(lambda: draw(win, grids, ROWS, size),
                                 grids, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grids = make_grids(ROWS, size)

    pygame.quit()


if __name__ == "__main__":
    main(WIN, SIZE)
