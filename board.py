from cell import Cell
from random import getrandbits


class Board:
    """Board represents the board that the game takes place on"""

    def __init__(self, rows, columns):
        """
        Contains the initialization logic for the board. Also prevents multiple boards from being created
        :param rows: the number of rows the board will have
        :param columns: the number of columns the board will have
        :return: a board with the specified number of rows and columns
        """
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for i in range(0, columns)] for j in range(0, rows)]

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def __str__(self):
        """Displays a string representation of the board"""
        returned = ''
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                returned += self._grid[i][j].__str__()
            returned += '\n'
        return returned

    def generate_random(self):
        """Populates the grid with cells that are randomly determined to be alive or dead"""
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if getrandbits(1):
                    self._grid[i][j].alive = True

    def _check_cell_neighbor(self, row: int, column: int) -> int:
        liveNeighbors = 0
        for i in range(row - 1, row + 2):
            # if cell that would be checked is outside the board, checks the cell on the opposite side of the board
            if i == -1:
                i = self._rows - 1
            elif i == (self._rows + 1):
                i = 0
            for j in range(column - 1, column + 2):
                if j == -1:
                    j = self._columns - 1
                elif j == (self._columns + 1):
                    j = 0
                if i != row or j != column:
                    if self._grid[i][j].alive:
                        liveNeighbors += 1
        return liveNeighbors

