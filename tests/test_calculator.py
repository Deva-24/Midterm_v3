# tests/test_calculator.py
import unittest
import os
from app.calculator import Calculator, CalculatorConfig

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        # Clear any existing history file
        if os.path.exists(os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv")):
            os.remove(os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv"))

    def test_execute_add(self):
        result = self.calculator.execute("add", 5, 3)
        self.assertEqual(result, 8)

    def test_save_and_load_history(self):
        self.calculator.execute("add", 1, 2)
        self.calculator.execute("multiply", 3, 4)
        self.calculator.save_history()
        # Reload history and check if it's preserved
        new_calculator = Calculator()
        new_calculator.load_history()
        self.assertEqual(len(new_calculator.history), 2)

    def tearDown(self):
        # Clean up saved files after each test
        if os.path.exists(os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv")):
            os.remove(os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv"))

if __name__ == "__main__":
    unittest.main()
