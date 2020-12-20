from Characters.AttackingCharacter import AttackingCharacter


class Player(AttackingCharacter):
    """
    Class representing the player who is playing the game
    """

    def __init__(self):
        AttackingCharacter.__init__(self)

    def __repr__(self):
        return f"Health: {self.health}\nInventory: {self.inventory}"

    def _ResetStats(self):
        self.health.SetNewMax(100)
        self.health.SetToMax()
