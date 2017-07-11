import unittest
from currency import Dollar


class TestHelpers(unittest.TestCase):

    def test_Multiplication(self):
        five = Dollar(5)

        self.assertEqual(Dollar(10).amount, five.times(2).amount)
        self.assertEqual(Dollar(15).amount, five.times(3).amount)


    def test_Equity(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))


if __name__=='__main__':
    unittest.main(verbosity=2)
