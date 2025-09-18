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

from src.calculator import multiply, divide

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12
    assert multiply(7, 8) == 56

def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 10) == 0

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(-4, -5) == 20

def test_divide_positive_numbers():
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5

def test_divide_by_zero_raises_error():
    import pytest
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(-12, -3) == 4
