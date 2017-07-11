import unittest
from currency import Dollar


class TestHelpers(unittest.TestCase):



    def test_Multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)



if __name__=='__main__':
    unittest.main(verbosity=2)
