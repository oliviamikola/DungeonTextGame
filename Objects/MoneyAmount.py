class MoneyAmount:
    """
    Class representation of a cost for an item or object
    """

    SilverInGold = 10

    def __init__(self, gold: int = 0, silver: int = 0):
        self.gold: int = gold
        self.silver: int = silver
        self.Format()

    def __str__(self):
        return f"{self.gold} Gold {self.silver} Silver"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.gold == other.gold and self.silver == other.silver

    def __gt__(self, amount):
        amountInSilver = self.silver + self.gold * MoneyAmount.SilverInGold
        otherAmountInSilver = amount.silver + amount.gold * MoneyAmount.SilverInGold
        return amountInSilver > otherAmountInSilver

    def __mul__(self, multiplier: int):
        return MoneyAmount(self.gold * multiplier, self.silver * multiplier)

    def Format(self):
        """
        Formats the gold and silver so there is no excess silver in the account
        All possible silver is converted to gold
        :return: None
        """
        self.gold += self.silver // MoneyAmount.SilverInGold
        self.silver %= MoneyAmount.SilverInGold

    def Add(self, amount) -> None:
        """
        Adds money to the account
        :param gold: amount of gold to add
        :param silver: amount of silver to add
        :return: None
        """
        self.silver += amount.silver
        self.gold += amount.gold
        self.Format()

    def Subtract(self, amount) -> bool:
        """
        Subtracts money from the account
        :param gold: amount of gold to subtract
        :param silver: amount of silver to subtract
        :return: True if transaction is possible, False otherwise
        """
        totalInSilver = self.silver + self.gold * MoneyAmount.SilverInGold

        toSubtractInSilver = amount.gold * MoneyAmount.SilverInGold + amount.silver
        totalInSilver -= toSubtractInSilver

        if totalInSilver < 0:
            return False

        self.silver = totalInSilver
        self.gold = 0
        self.Format()
        return True
