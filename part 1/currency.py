class Expression():
    def reduce(self, bank, to):
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


    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)


class Bank():
    def reduce(self, source, to):
        return source.reduce(self, to)


    def rate(self, fromCurr, toCurr):
        return 2 if fromCurr == 'CHF' and toCurr == 'USD' else 1


class Sum(Expression):
    def __init__(self, augend, addend):
        self.addend = addend
        self.augend = augend


    def reduce(self, bank, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class Pair():
    def __init__(self, fromC, toC):
        self.fromC = fromC
        self.toC = toC


    def equals(self, object):
        pair = Pair()



    def hashcode(self):
        return 0

