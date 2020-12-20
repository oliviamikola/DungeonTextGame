class MaxTracker:
    """
    Class to store a max value and an adjustable value that will never exceed the max
    """

    def __init__(self, maxValue: int, startLow: bool = True):
        self.max = maxValue
        self.adjustable = 0

        if not startLow:
            self.SetToMax()

    def __repr__(self):
        return f"{self.adjustable}/{self.max}"

    def __lt__(self, other):
        if type(other) == int or type(other) == float:
            return self.adjustable < other

    def __le__(self, other):
        if type(other) == int or type(other) == float:
            return self.adjustable <= other

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            return self.adjustable > other

    def __ge__(self, other):
        if type(other) == int or type(other) == float:
            return self.adjustable >= other

    def AdjustUp(self, increment: int = 1):
        """
        Adjusts the value up by increment
        If the new adjustable value exceeds the max value, the adjustable will be set to max
        :param increment: value to increment up by
        :return: None
        """
        self.adjustable = min(self.adjustable + increment, self.max)

    def AdjustDown(self, increment: int = 1):
        """
        Adjusts the value down by increment
        If the new adjustable value is less than 0, the adjustable will be set to 0
        :param increment: value to increment down by
        :return: None
        """
        self.adjustable = max(self.adjustable - increment, 0)

    def AtMax(self):
        """
        Checks if the adjustable value is at the max allowed value
        :return: True if adjustable is at max value, False otherwise
        """
        return self.adjustable == self.max

    def AtZero(self):
        """
        Checks if the adjustable value is at zero
        :return: True if adjustable is at zero, False otherwise
        """
        return self.adjustable == 0

    def SetToMax(self):
        """
        Sets the adjustable value to the max allowed value
        :return: None
        """
        self.adjustable = self.max

    def SetToZero(self):
        """
        Sets the adjustable value to zero
        :return: None
        """
        self.adjustable = 0

    def SetNewMax(self, newMax):
        """
        Sets the max value to a new max value
        :param newMax: value to set max to
        :return: None
        """
        self.max = newMax
