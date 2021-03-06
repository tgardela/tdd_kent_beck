import unittest
from currency import Money, Bank, Sum, Expression


class TestHelpers(unittest.TestCase):

    def test_Multiplication(self):
        five = Money.dollar(5)

        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))


    def test_Equity(self):
        self.assertTrue(Money.dollar(5).equals(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).equals(Money.dollar(6)))

        self.assertFalse(Money.franc(5).equals(Money.dollar(5)))


    def test_Currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())
        self.assertEqual('CHF', Money.franc(1).currency())


    def test_SimpleAddition(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        self.assertEqual(reduced, Money.dollar(10))


    def test_PlusReturnsSum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)


    def test_Reduce_Sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, 'USD')
        self.assertEqual(Money.dollar(7), result)


    def test_ReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)


    def test_ReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(Money.dollar(1), result)




if __name__=='__main__':
    unittest.main(verbosity=2)
