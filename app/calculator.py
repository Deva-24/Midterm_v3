# app/calculator.py
import os
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
        self.current_index = -1  # Track the current operation for undo/redo functionality
        os.makedirs(CalculatorConfig.CALCULATOR_BASE_DIR, exist_ok=True)

    def _record_history(self, operation, a, b, result):
        entry = {
            "operation": operation,
            "operands": [a, b],
            "result": result
        }
        
        # When adding a new entry, discard any 'redo' entries if we're mid-history
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]
        
        # Append the new entry to history and adjust the index
        self.history.append(entry)
        if len(self.history) > CalculatorConfig.CALCULATOR_MAX_HISTORY_SIZE:
            self.history.pop(0)
        self.current_index = len(self.history) - 1

        if CalculatorConfig.CALCULATOR_AUTO_SAVE:
            self.save_history()

    def execute(self, operation, a, b):
        method = getattr(self.operations, operation, None)
        if not method:
            raise ValueError("Operation not supported.")
        result = method(a, b)
        self._record_history(operation, a, b, result)
        return result

    def undo(self):
        if self.current_index <= 0:
            print("Nothing to undo.")
            return None
        self.current_index -= 1
        entry = self.history[self.current_index]
        print(f"Undone: {entry['operation']}({entry['operands'][0]}, {entry['operands'][1]}) = {entry['result']}")
        return entry

    def redo(self):
        if self.current_index >= len(self.history) - 1:
            print("Nothing to redo.")
            return None
        self.current_index += 1
        entry = self.history[self.current_index]
        print(f"Redone: {entry['operation']}({entry['operands'][0]}, {entry['operands'][1]}) = {entry['result']}")
        return entry

    def save_history(self):
        df = pd.DataFrame(self.history)
        df.to_csv(os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv"), index=False)

    def load_history(self):
        path = os.path.join(CalculatorConfig.CALCULATOR_BASE_DIR, "history.csv")
        if os.path.exists(path):
            self.history = pd.read_csv(path).to_dict(orient='records')
            self.current_index = len(self.history) - 1
