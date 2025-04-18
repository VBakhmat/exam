import unittest
from main import factorial

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_raises_error_on_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == "__main__":
    unittest.main()
