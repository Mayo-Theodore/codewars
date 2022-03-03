import pytest
from tribonacci import * 

def test_n():
    assert n([1,1,0], 5) == [1,1,0,1,1]

def test_tribonacci():
    # assert tribonacci([0, 0, 1], 5) == [0, 0, 1, 1, 2]
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
