from dataclasses import dataclass


@dataclass
class Dimensions:
    """
    Data class to handle the UI dimensions
    """

    WIDTH = 800
    HEIGHT = 800


@dataclass
class Interface:
    """
    Data class to handle the interface properties
    """

    BLOCK_SIZE = 50
