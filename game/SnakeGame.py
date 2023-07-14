import pygame
from pygame.event import Event


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

        while self.game_running:
            for event in pygame.event.get():
                self._check_game_is_over(event=event)

    def _init_game(self) -> None:
        """
        Inject initial properties of the video game
        """

        pygame.time.Clock()

        self.display = pygame.display.set_mode(size=(600, 600))
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
