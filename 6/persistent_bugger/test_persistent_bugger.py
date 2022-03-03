import pytest
from persistent_bugger import *

def test_number_of_digits():
    assert number_of_digits(4) == 1

def test_persistence():
    assert persistence(999) == 4
    assert persistence(39) == 3

# def test_persistence_second():
#     assert persistence_second(999) == 729


