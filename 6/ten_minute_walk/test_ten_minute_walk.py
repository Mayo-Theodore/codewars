import pytest
from ten_minute_walk import *

def test_length_of_walk():
    assert is_ten_mins(['n','n','n','n','n','n','n','n','n','n']) == 10

def test_starting_point():
    assert starting_point(['n','n','n','n','n','n','n','n','n','n']) == False
    assert starting_point(['n','s','n','s','n','s','n','s','n','s']) == True
    assert starting_point(['w','e','w','e','w','e','w','e','w','e','w','e']) == False
    assert starting_point(['w']) == False
    assert starting_point(['n','n','n','s','n','s','n','s','n','s']) == False


