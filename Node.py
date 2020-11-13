import pygame
import Colors as C


class Node:
    def __init__(self, column, width, height, total_columns, WINDOW_WIDTH, WINDOW_HEIGHT):
        # the color is a tuple of RGB from Colors
        # White is the color of a node that is open, one that hasn't been looked at yet
        self.color = C.GREY

        # column is the position from left to right
        self.column = column

        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT

        # the x and y of the Node, the top left corner
        # x is the position times the width of each node
        # since columns will be drawn from bottom up, it is the height of the window - the height of the node
        self.x = column * width
        self.y = WINDOW_HEIGHT - height

        # width of the node
        self.width = width

        # height of the node
        self.height = height

        # total number of rows in the grid
        self.total_columns = total_columns

    # getters
    def get_color(self):
        return self.color

    def get_column(self):
        return self.column

    def get_window_width(self):
        return self.window_width

    def get_window_height(self):
        return self.window_height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_total_columns(self):
        return self.total_columns

    # setters
    def set_column(self, column):
        self.column = column

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # draw the Node
    def draw(self, win):
        pygame.draw.rect(win, self.get_color(), (self.get_x(), self.get_y(), self.get_width(), self.get_height()))
