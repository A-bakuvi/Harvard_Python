"""
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello guy") == 0
    assert value("hello!") == 0
def test_h():
    assert value("hey") == 20
    assert value("how are you?") == 20
    assert value("hey!@#") == 20
def test_other():
    assert value("whats up") == 100
    assert value("good evening!!") == 100
    assert value("well hello @#$%") == 100
def test_case_insensitivity():
    assert value("Hello") == 0
    assert value("hELLo") == 0
    assert value("HELLO") == 0
    assert value("hElLo") == 0
"""