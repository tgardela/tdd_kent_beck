import unittest
import fib


class TestFibonacchi(unittest.TestCase):
    def test_FibRetZero(self):
        self.assertEqual(0, fib.fibonacchi(0))







if __name__=='__main__':
    unittest.main(verbosity=2)