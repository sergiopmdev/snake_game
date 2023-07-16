import random

import pygame
from pygame.event import Event

from game.constants import Dimensions, Interface
from game.Snake import Snake


class SnakeGame:
    """
    SnakeGame class that manages the
    video game interface and logic

    Attributes
    ----------
    game_running : bool
        True if the game should be running and
        False if the game should be terminated
    """

    def __init__(self) -> None:
        """
        SnakeGame class initializer
        """

        self.game_running = True

    def run_game(self) -> None:
        """
        Run the video game and keep
        it active until it is closed
        """

        self._init_game()
        self._draw_grid()

        self._snake = Snake()
        self._generate_apple()

        while self.game_running:
            for event in pygame.event.get():
                self._check_game_is_over(event=event)
                self._snake.change_direction(event=event)

            self._draw_grid()
            self._plot_snake_and_apple()
            self._snake.move()

            if self._snake.check_self_collision():
                self.game_running = False

            if self._snake.eat_apple(self._apple):
                self._generate_apple()

            self._check_if_snake_out_of_bounds()

            pygame.display.update()
            self._clock.tick(10)

    def _init_game(self) -> None:
        """
        Inject initial properties of the video game
        """

        self._clock = pygame.time.Clock()
        self._display = pygame.display.set_mode((Dimensions.WIDTH, Dimensions.HEIGHT))

        pygame.display.set_caption("Snake Game")

    def _draw_grid(self) -> None:
        """
        Draw the grid of squares inside the interface
        """

        self._display.fill("black")

        for x in range(0, Dimensions.WIDTH, Interface.BLOCK_SIZE):
            for y in range(0, Dimensions.HEIGHT, Interface.BLOCK_SIZE):
                square = pygame.Rect(x, y, Interface.BLOCK_SIZE, Interface.BLOCK_SIZE)
                pygame.draw.rect(self._display, "grey", square, 1)

    def _check_game_is_over(self, event: Event) -> None:
        """
        Check if the current event of
        the video game is to close it

        Parameters
        ----------
        event : Event
            Video game event
        """

        if event.type == pygame.QUIT:
            self.game_running = False

    def _plot_snake_and_apple(self) -> None:
        """
        Draw the snake in its corresponding
        position in the video game UI grid
        """

        pygame.draw.rect(self._display, "green", self._snake.head)

        for square in self._snake.body:
            pygame.draw.rect(self._display, "green", square)

        pygame.draw.rect(self._display, "red", self._apple)

    def _check_if_snake_out_of_bounds(self) -> None:
        """
        Checks if the snake is out of bounds
        based on its x and y coordinates
        """

        out_of_bounds_x = self._snake.head.x in (
            Dimensions.WIDTH,
            -Interface.BLOCK_SIZE,
        )

        out_of_bounds_y = self._snake.head.y in (
            Dimensions.HEIGHT,
            -Interface.BLOCK_SIZE,
        )

        if out_of_bounds_x or out_of_bounds_y:
            self.game_running = False

    def _generate_apple(self) -> None:
        """
        Generates an apple at a random position
        on the grid excluding the positions
        taken by the snake
        """

        x_numbers_to_exclude = []
        y_numbers_to_exclude = []

        x_numbers_to_exclude.append(self._snake.head.x)
        y_numbers_to_exclude.append(self._snake.head.y)

        for square in self._snake.body:
            x_numbers_to_exclude.append(square.x)
            y_numbers_to_exclude.append(square.y)

        available_x_postions = list(
            set(list(range(0, Dimensions.WIDTH, Interface.BLOCK_SIZE)))
            - set(x_numbers_to_exclude)
        )

        available_y_postions = list(
            set(list(range(0, Dimensions.HEIGHT, Interface.BLOCK_SIZE)))
            - set(y_numbers_to_exclude)
        )

        x_apple = random.choice(available_x_postions)
        y_apple = random.choice(available_y_postions)

        self._apple = pygame.Rect(
            x_apple, y_apple, Interface.BLOCK_SIZE, Interface.BLOCK_SIZE
        )
