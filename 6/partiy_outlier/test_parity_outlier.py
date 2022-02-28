import pytest
from parity_outlier import *

def test_integer_from_list():
    assert type(an_integer([5, 6, 7])) is int

def test_integer_type():
    assert integer_type([3, 5, 7, 8]) == "Odd"

def test_outlier():
    assert outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
