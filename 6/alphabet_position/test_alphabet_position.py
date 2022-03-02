import pytest
from alphabet_position import *

def test_alphabet_position():
    assert alphabet_position('a') == "1"
    assert alphabet_position('a1%') == "1"
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def test_all_letters():
    assert all_letters("2747ab") == False
    assert all_letters("adfb") == True
