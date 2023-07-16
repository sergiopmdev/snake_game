import pygame
from pygame import Rect
from pygame.event import Event

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

    def change_direction(self, event: Event) -> None:
        """
        Change direction of the snake
        according to the keys on the keypad

        Parameters
        ----------
        event : Event
            Event in which it is checked whether
            a motion key has been activated
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.x_dir = 0
                self.y_dir = -1 if self.y_dir != 1 else self.y_dir
            elif event.key == pygame.K_RIGHT:
                self.x_dir = 1 if self.x_dir != -1 else self.x_dir
                self.y_dir = 0
            elif event.key == pygame.K_DOWN:
                self.x_dir = 0
                self.y_dir = 1 if self.y_dir != -1 else self.y_dir
            elif event.key == pygame.K_LEFT:
                self.x_dir = -1 if self.x_dir != 1 else self.x_dir
                self.y_dir = 0

    def eat_apple(self, apple: Rect) -> bool:
        """
        Determines if the snake's head is colliding
        with the given apple. If there is a collision,
        the snake's body is extended by adding a new segment

        Parameters
        ----------
        apple : Rect
            The rectangular representation of the apple

        Returns
        -------
        bool
            True if the snake's head collides with the
            apple and the body is extended,
            False otherwise
        """

        same_x = self.head.x == apple.x
        same_y = self.head.y == apple.y

        if same_x and same_y:
            snake_tail = self.body[0]

            new_x = snake_tail.x
            new_y = snake_tail.y

            if self.x_dir == 1:
                new_x -= Interface.BLOCK_SIZE
            elif self.x_dir == -1:
                new_x += Interface.BLOCK_SIZE
            elif self.y_dir == 1:
                new_y -= Interface.BLOCK_SIZE
            elif self.y_dir == -1:
                new_y += Interface.BLOCK_SIZE

            self.body.insert(
                0,
                Rect(new_x, new_y, Interface.BLOCK_SIZE, Interface.BLOCK_SIZE),
            )

            return True

        return False
