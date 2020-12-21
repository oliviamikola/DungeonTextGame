from typing import List
from Characters.Monster import Monster


class Room:
    """
    Class representing a room in a dungeon
    """

    def __init__(self):
        self.discovered = False
        self.monsters: List[Monster] = []
        self.connectedRooms: List[Room] = []
