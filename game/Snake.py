from pygame import Rect

from game.constants import Interface

###########################
# SNAKE PROPERTIES FACADE #
###########################

X = Y = Interface.BLOCK_SIZE
HEAD = Rect(X, Y, Interface.BLOCK_SIZE, Interface.BLOCK_SIZE)
BODY = [Rect(X - Interface.BLOCK_SIZE, Y, Interface.BLOCK_SIZE, Interface.BLOCK_SIZE)]
X_DIR, Y_DIR = 1, 0
DEAD = False


class Snake:
    """
    Snake class that manages both the
    properties and the logic of the
    snake within the video game

    Attributes
    ----------
    x : int
        Position on x-axis
    y : int
        Position on y-axis
    head : Rect
        Snake head inside the grid
    body : Rect
        Body head inside the grid
    x_dir : int
        Horizontal movement
    y_dir : int
        Vertical movement
    dead : bool
        The snake is dead or not dead
    """

    def __init__(self) -> None:
        """
        Snake class initializer
        """

        self.x = X
        self.y = Y
        self.head = HEAD
        self.body = BODY
        self.x_dir = X_DIR
        self.y_dir = Y_DIR
        self.dead = DEAD
