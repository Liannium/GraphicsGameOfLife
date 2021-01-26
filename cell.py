class Cell:
    """Cell represents an individual cell in the game"""
    def __init__(self):
        """initializes a cell to be dead"""
        self.alive = False

    def __str__(self):
        """
        Displays a string representation of the cell
        :return: a shaded block if the cell is alive, and a space if the cell is dead
        """
        if self.alive:
            return "\u2588 "
        else:
            return "  "
