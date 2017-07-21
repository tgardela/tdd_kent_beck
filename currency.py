class Expression():
    pass

class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency


    def equals(self, money):
        return self._amount == money._amount and self.currency() == money.currency()


    def __eq__(self, money):
        return self.__dict__ == money.__dict__


    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')


    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


    def currency(self):
        return self._currency


    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)


    def plus(self, addend):
        return Sum(self, addend)


class Bank():
    @staticmethod
    def reduce(source, to):
        sum = source
        amount = sum.augend._amount + sum.addend._amount
        return Money(amount, to)


class Sum(Expression):
    def __init__(self, augend, addend):
        self.addend = addend
        self.augend = augend





