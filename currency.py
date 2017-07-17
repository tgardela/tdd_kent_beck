class Money():
    def __init__(self, amount):
        self.amount = amount


    def equals(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__


    def __eq__(self, money):
        return self.__dict__ == money.__dict__

    @staticmethod
    def dollar(amount):
        return Dollar(amount)


    @staticmethod
    def franc(amount):
        return Franc(amount)


    def currency(self):
        pass



class Dollar(Money):
    def __init__(self, amount):
        super(Dollar, self).__init__(amount)
        self._currency = 'USD'

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def currency(self):
        return self._currency


class Franc(Money):

    def __init__(self, amount):
        super(Franc, self).__init__(amount)
        self._currency = 'CHF'


    def times(self, multiplier):
        return Franc(self.amount * multiplier)


    def currency(self):
        return self._currency
