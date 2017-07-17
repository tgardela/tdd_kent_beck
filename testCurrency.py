import unittest
from currency import Money


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


if __name__=='__main__':
    unittest.main(verbosity=2)
