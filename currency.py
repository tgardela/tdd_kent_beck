class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency


    def equals(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__


    def __eq__(self, money):
        return self.__dict__ == money.__dict__


    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')


    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')


    def currency(self):
        return self._currency



class Dollar(Money):
    def __init__(self, amount, currency):
        super(Dollar, self).__init__(amount, currency)


    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)



class Franc(Money):
    def __init__(self, amount, currency):
        super(Franc, self).__init__(amount, currency)


    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)



