import pytest
import os
from calculator.operations import add, subtract, multiply, divide, exponentiate


# Test for add
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


# Test for subtract
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, -3) == -2
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0


# Test for multiply
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(0, 100) == 0
    assert multiply(1.5, 2) == 3.0


# Test for divide
def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(1, 2) == 0.5
    with pytest.raises(ValueError):  # Test for division by zero
        divide(10, 0)


# Test for exponentiate
def test_exponentiate_enabled():
    # Enable advanced mode
    os.environ['ENABLE_ADVANCED'] = 'True'
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 0) == 1
    assert exponentiate(2, -1) == 0.5


def test_exponentiate_disabled():
    # Disable advanced mode
    if 'ENABLE_ADVANCED' in os.environ:
        del os.environ['ENABLE_ADVANCED']
    with pytest.raises(KeyError):
        exponentiate(2, 3)
