# tests/test_operations.py
import pytest
from app.operations import Operations

@pytest.fixture
def operations():
    return Operations()

def test_add(operations):
    assert operations.add(5, 3) == 8

def test_subtract(operations):
    assert operations.subtract(5, 3) == 2

def test_multiply(operations):
    assert operations.multiply(5, 3) == 15

def test_divide(operations):
    assert operations.divide(6, 3) == 2

def test_divide_by_zero(operations):
    with pytest.raises(ZeroDivisionError):
        operations.divide(5, 0)

def test_power(operations):
    assert operations.power(2, 3) == 8

def test_root(operations):
    assert operations.root(9, 2) == 3

def test_root_negative_number(operations):
    with pytest.raises(ValueError):  # Assuming root of negative is invalid
        operations.root(-9, 2)
