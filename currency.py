class Money():
    def __init__(self, amount):
        self.amount = amount


    def equals(self, money):
        return self.amount == money.amount


    def __eq__(self, money):
        return self.__dict__ == money.__dict__



class Dollar(Money):

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
