import pytest
from persistent_bugger import *

def test_number_of_digits():
    assert number_of_digits(4) == 1

def test_persistence():
    assert persistence(999) == 729
    assert persistence(729) == 126

# def test_persistence_second():
#     assert persistence_second(999) == 729


