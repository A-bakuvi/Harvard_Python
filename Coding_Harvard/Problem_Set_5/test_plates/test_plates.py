"""
from plates import is_valid

def test_valid_plates():
    assert is_valid("AA") == True
    assert is_valid("ABC123") == True
    assert is_valid("AA2222") == True

def test_letters():
    #assert is_valid("AA") == True
    assert is_valid("1A") == False
    assert is_valid("A1222") == False

def test_zero():
    assert is_valid("AA012") == False
   # assert is_valid("AA10") == True

def test_number_In_middle():
   # assert is_valid("AA1") == True
    assert is_valid("A111A") == False
    assert is_valid("A1A") == False
    assert is_valid("AA123A") == False

def test_len():
   # assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAA1") == False

def test_grammar():
    assert is_valid("A..??A") == False
    assert is_valid("AA,.AA") == False
    assert is_valid("AAA??") == False
"""