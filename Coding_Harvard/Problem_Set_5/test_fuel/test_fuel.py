"""
from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"

def test_convert():

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("10/9")
    with pytest.raises(ValueError):
        convert("1/c")
    with pytest.raises(ValueError):
        convert("c/1")
    with pytest.raises(ValueError):
        convert("v/c")
    with pytest.raises(ValueError):
        convert("1")
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("0/100") == 0
    assert convert("100/100") == 100
"""