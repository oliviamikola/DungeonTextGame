from Characters.AttackingCharacter import AttackingCharacter


class Monster(AttackingCharacter):
    """
    Base class for all monsters
    """
    def __init__(self):
        AttackingCharacter.__init__(self)

    def _ResetStats(self):
        self.health = 60

    def Attack(self):
        """
        Attacks the player if player is visible to the monster
        :return:
        """
        pass

    def Drop(self):
        """
        Decides what the monster drops upon death
        :return:
        """
        pass
