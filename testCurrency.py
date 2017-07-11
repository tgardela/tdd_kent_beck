import unittest
from currency import Dollar


class TestHelpers(unittest.TestCase):



    def test_Multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)

        product = five.times(3)
        self.assertEqual(15, product.amount)




if __name__=='__main__':
    unittest.main(verbosity=2)
