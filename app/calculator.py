# app/calculator.py
import os
import json
import pandas as pd
from app.operations import Operations

class CalculatorConfig:
    CALCULATOR_BASE_DIR = os.getenv("CALCULATOR_BASE_DIR", "./calculator_data")
    CALCULATOR_MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
    CALCULATOR_AUTO_SAVE = bool(int(os.getenv("CALCULATOR_AUTO_SAVE", 1)))

class Calculator:
    def __init__(self):
        self.operations = Operations()
        self.history = []
        os.makedirs(CalculatorConfig.CALCULATOR_BASE_DIR, exist_ok=True)

    def _record_history(self, operation, a, b, result):
        entry = {
            "operation": operation,
            "operands": [a, b],
            "result": result
        }
        if len(self.history) >= CalculatorConfig.CALCULATOR_MAX_HISTORY_SIZE:
            self.history.pop(0)
        self.history.append(entry)
        if CalculatorConfig.CALCULATOR_AUTO_SAVE:
            self.save_history()

    def execute(self, operation, a, b):
        method = getattr(self.operations, operation, None)
        if not method:
            raise ValueError("Operation not supported.")
        result = method(a, b)
        self._record_history(operation, a, b, result)
        return result

    def save_history(self):
        df = pd.DataFrame(self.history)
        df.to_csv(os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv"), index=False)

    def load_history(self):
        path = os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv")
        if os.path.exists(path):
            self.history = pd.read_csv(path).to_dict(orient='records')
