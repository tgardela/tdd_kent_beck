import unittest
import fib


class TestFibonacchi(unittest.TestCase):
    def test_Fibonacchi(self):
        testCases = [[0,0], [1,1], [1,2], [2,3]]
        for i in range(0, len(testCases)):
            self.assertEqual(testCases[i][0], fib.fibonacchi(testCases[i][1]))


if __name__=='__main__':
    unittest.main(verbosity=2)