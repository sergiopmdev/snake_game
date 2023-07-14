import pygame
from pygame.event import Event

from game.constants import Dimensions


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

        while self.game_running:
            for event in pygame.event.get():
                self._check_game_is_over(event=event)
            pygame.display.update()
            self._clock.tick(10)

    def _draw_grid(self) -> None:
        """
        Draw the grid of squares inside the interface
        """

        BLOCK_SIZE = 50

        for x in range(0, Dimensions.WIDTH, BLOCK_SIZE):
            for y in range(0, Dimensions.HEIGHT, BLOCK_SIZE):
                grid = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self._display, "grey", grid, 1)

    def _init_game(self) -> None:
        """
        Inject initial properties of the video game
        """

        self._clock = pygame.time.Clock()
        self._display = pygame.display.set_mode((Dimensions.WIDTH, Dimensions.HEIGHT))

        pygame.display.set_caption("Snake Game")

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
