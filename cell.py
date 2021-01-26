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

    def should_survive(self, live_neighbors: int) -> bool:
        if self.alive:
            if live_neighbors < 2 or live_neighbors > 3:
                return False
        elif not self.alive:
            if live_neighbors == 3:
                return True
        return self.alive
