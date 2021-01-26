class Cell:
    """Cell represents an individual cell in the game"""
    def __init__(self, alive: bool):
        """
        initializes the cell to its starting value
        :param alive: whether the cell should be initialized as alive or dead
        """
        self._alive = alive

    def __str__(self):
        """
        Displays a string representation of the cell
        :return: a shaded block if the cell is alive, and a space if the cell is dead
        """
        if self._alive:
            return "\u2588"
        else:
            return " "
