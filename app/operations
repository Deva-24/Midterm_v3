# app/operations.py
import pandas as pd

class Operations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def root(self, a, b):
        if a < 0:
            raise ValueError("Cannot take root of a negative number.")
        return a ** (1 / b)

    def to_dataframe(self, history):
        # Convert history to pandas DataFrame for better formatting and export options
        return pd.DataFrame(history)
