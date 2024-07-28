from twttr import shorten

def test_without_vowel():
    assert shorten("bthgd") == "bthgd"
def test_vowels():
    assert shorten("cats") == "cts"
def test_nonLetter():
    assert shorten("1!") == "1!"
def test_uppercase():
    assert shorten("CAT") == "CT"
def test_emtyStr():
    assert shorten("") == ""


# test for non-letters
# test uppercase - lowercase
# test emty str