# tests/test_calculator.py
import pytest
import pandas as pd
from app.calculator import Calculator
import tempfile
import os  # Make sure os is imported


@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    result = calculator.execute("add", 5, 3)
    assert result == 8

def test_subtract(calculator):
    result = calculator.execute("subtract", 5, 3)
    assert result == 2

def test_multiply(calculator):
    result = calculator.execute("multiply", 5, 3)
    assert result == 15

def test_divide(calculator):
    result = calculator.execute("divide", 6, 3)
    assert result == 2

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.execute("divide", 5, 0)

def test_power(calculator):
    result = calculator.execute("power", 2, 3)
    assert result == 8

def test_root(calculator):
    result = calculator.execute("root", 9, 2)
    assert result == 3

def test_undo(calculator):
    calculator.execute("add", 5, 3)
    calculator.execute("subtract", 8, 2)
    calculator.undo()
    assert calculator.history[calculator.current_index]["operation"] == "add"

def test_redo(calculator):
    calculator.execute("add", 5, 3)
    calculator.execute("subtract", 8, 2)
    calculator.undo()
    calculator.redo()
    assert calculator.history[calculator.current_index]["operation"] == "subtract"


def test_save_and_load_history():
    # Create a Calculator instance
    calc = Calculator()

    # Perform some operations using execute, not add directly
    calc.execute("add", 5, 3)
    calc.execute("subtract", 10, 4)

    # Use a temporary directory to save the history file
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = f"{temp_dir}/history.csv"
        calc.save_history(temp_file)  # Pass temp_file path
        
        # Check if the file was created and saved
        assert os.path.exists(temp_file), "History file was not created."

        # Load the history from the file and check contents
        calc.load_history(temp_file)
        history_df = pd.read_csv(temp_file)
        assert len(history_df) == 2, "History data does not match expected entries."