class Dollar():
    def __init__(self, amount):
        self.amount = amount


    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


    def equals(self, dollar):
        return self.amount == dollar.amount

    def __eq__(self, dollar):
        return self.__dict__ == dollar.__dict__


class Franc():
    def __init__(self, amount):
        self.amount = amount


    def times(self, multiplier):
        return Franc(self.amount * multiplier)


    def equals(self, franc):
        return self.amount == franc.amount

    def __eq__(self, franc):
        return self.__dict__ == franc.__dict__