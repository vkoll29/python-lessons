import unittest
from algos.memoization import fib

class TestFib(unittest.TestCase):
    def test_two(self):
        """
        test that any positive value less than or equal to two will return 1
        """
        self.assertEqual(fib(2), 1)


if __name__ == '__main__':
    unittest.main()

    