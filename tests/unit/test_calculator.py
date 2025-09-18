"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, subtract, divide, multiply  # add multiply import

class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


# ✅ your new tests go OUTSIDE the class:
def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2

def test_add_negative_numbers():
    """Test adding negative numbers"""
    from src.calculator import add
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2

def test_subtract_negative_numbers():
    """Test subtracting negative numbers"""
    from src.calculator import subtract
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2
