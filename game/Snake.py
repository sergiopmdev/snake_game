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

    def move(self) -> None:
        """
        Move the snake steadily based on the
        horizontal and vertical direction values
        """

        self.body.append(self.head)

        for index in range(len(self.body) - 1):
            self.body[index].x = self.body[index + 1].x
            self.body[index].y = self.body[index + 1].y

        self.head.x += self.x_dir * Interface.BLOCK_SIZE
        self.head.y += self.y_dir * Interface.BLOCK_SIZE

        self.body.remove(self.head)
