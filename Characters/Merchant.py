from Characters.Character import Character
import sys


class Merchant(Character):
    """
    Class representation of the merchant
    """

    def __init__(self):
        Character.__init__(self)

    def _ResetStats(self):
        self.health = sys.maxsize
        self.attackable = False
