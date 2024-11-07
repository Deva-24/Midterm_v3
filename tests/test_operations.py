# tests/test_operations.py
import unittest
from app.operations import Operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.operations = Operations()

    def test_addition(self):
        self.assertEqual(self.operations.add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.operations.subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.operations.multiply(5, 3), 15)

    def test_division(self):
        self.assertEqual(self.operations.divide(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            self.operations.divide(6, 0)

    def test_power(self):
        self.assertEqual(self.operations.power(2, 3), 8)

    def test_root(self):
        self.assertEqual(self.operations.root(9, 2), 3)
        with self.assertRaises(ValueError):
            self.operations.root(-9, 2)
