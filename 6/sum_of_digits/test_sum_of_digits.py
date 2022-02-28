import pytest
from sum_of_digits import *

def test_number_of_digits():
    assert digit_check(1) == "Please enter a minimum of 2 digits"

def test_sum_of_number():
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2

    

    

