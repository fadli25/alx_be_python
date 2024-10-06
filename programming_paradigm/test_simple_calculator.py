import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Positive and negative
        self.assertEqual(self.calc.add(-5, -5), -10)  # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Zeros
    
    # You can add other test methods similarly:
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 5), -10)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero returns None

if __name__ == '__main__':
    unittest.main()
