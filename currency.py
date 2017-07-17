class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency


    def equals(self, money):
        return self.amount == money.amount and self.currency() == money.currency()


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


    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)



class Dollar(Money):
    def __init__(self, amount, currency):
        super(Dollar, self).__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount, currency):
        super(Franc, self).__init__(amount, currency)






