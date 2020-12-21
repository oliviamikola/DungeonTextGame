from Characters.Character import Character
from Helpers.MaxTracker import MaxTracker


class AttackingCharacter(Character):
    """
    Class representing an attacking character
    """

    def __init__(self):
        Character.__init__(self)
        self.health = MaxTracker(20, startLow=False)
        self._ResetStats()

    def _ResetStats(self):
        pass

    def Attack(self):
        pass
