import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_operations_together(self):
        calc = Calculator()
        result = calc.add(2, 3) * calc.multiply(2, 3)
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()

