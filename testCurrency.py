import unittest
from currency import Dollar, Franc


class TestHelpers(unittest.TestCase):

    def test_Multiplication(self):
        five = Dollar(5)

        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))


    def test_FrancMultiplication(self):
        five = Franc(5)

        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))


    def test_Equity(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))
        self.assertTrue(Franc(5).equals(Franc(5)))
        self.assertFalse(Franc(5).equals(Franc(6)))
        self.assertFalse(Franc(5).equals(Franc(6)))


if __name__=='__main__':
    unittest.main(verbosity=2)
