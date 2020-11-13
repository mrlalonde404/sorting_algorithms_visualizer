
import pygame
from random import shuffle
from Node import Node
import Colors as C

# constants for game
WIDTH = 800
NUM_NODES = 80
# makes sure that there is a screen with a width wider than the number of nodes or otherwise display results should
# get weird
if NUM_NODES > WIDTH:
    NUM_NODES = int(WIDTH / 2)

# global variables
global window
global started
# if the grid is sorted
global grid_sorted


# function that creates the pygame window and sets it up
def setup():
    global window
    pygame.init()
    window = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sorting Algorithms")
    window.fill(C.WHITE)
    pygame.display.update()


def draw(win, grid, nodes, width):
    # essentially refresh the screen by putting a blank canvas
    win.fill(C.WHITE)
    # draw each square Node onto the window canvas
    for node in grid:
        node.draw(win)
    draw_grid_lines(win, nodes, width)
    # update the window screen
    pygame.display.update()


def make_grid(nodes, width, heights):
    grid = []
    # gap is the width of the Node
    gap = width // nodes
    for i in range(nodes):
        # make the Node with column, width, height, total_columns, WINDOW_WIDTH, WINDOW_HEIGHT
        n = Node(i, gap, heights[i], nodes, WIDTH, WIDTH)
        grid.append(n)
    return grid


# these are the lines that are between all of the Nodes that split them up and define them
def draw_grid_lines(win, nodes, width):
    # gap is the width of the Node
    gap = width // nodes

    # draw the vertical lines
    for j in range(nodes):
        pygame.draw.line(win, C.BLACK, (j * gap, 0), (j * gap, width))


def get_random_node_heights(width, num_nodes):
    nodes = []
    gap = width // num_nodes

    # generates a num_nodes amount of heights
    for i in range(1, num_nodes + 1):
        height = gap * i
        nodes.append(height)

    # mix up the node's heights
    shuffle(nodes)
    return nodes


# swaps the node j in grid with the next node in the grid
def swap_nodes(grid, j):
    # swap column attributes
    grid[j].column, grid[j + 1].column = grid[j + 1].column, grid[j].column
    # swap x attributes
    grid[j].x, grid[j + 1].x = grid[j + 1].x, grid[j].x
    # swap spots in the grid
    grid[j], grid[j + 1] = grid[j + 1], grid[j]
    # return the altered grid
    return grid


def bubble_sort(grid):
    print("bubble sort started")
    # For all nodes in the grid, sort them by height
    for i in range(len(grid)):
        # Last i elements are already in place
        for j in range(len(grid) - i - 1):
            # If the left element has a bigger height than the right, swap them
            if grid[j].height > grid[j + 1].height:
                grid = swap_nodes(grid, j)
                # draw the new window everytime
                draw(window, grid, grid[j].total_columns, WIDTH)


def main():
    global window
    global started
    global grid_sorted
    setup()

    # get the random heights of the rectangles
    heights = get_random_node_heights(WIDTH, NUM_NODES)
    grid_sorted = False

    # make an initial grid
    grid = make_grid(NUM_NODES, WIDTH, heights)

    # keeps the game loop going
    run = True
    # if the user started the search or not
    started = False

    while run:

        # refresh the screen every time this loops, draw all the nodes, draw all the grid lines, update the screen
        draw(window, grid, NUM_NODES, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if left click, start the search and changed the started boolean
            if pygame.mouse.get_pressed()[0]:
                if not started:
                    # start the search
                    started = True
                    bubble_sort(grid)
                    started = False
                    grid_sorted = True

            # if the user started the search they shouldn't be able to do anything else below
            if started:
                continue

    pygame.quit()


if __name__ == "__main__":
    main()
