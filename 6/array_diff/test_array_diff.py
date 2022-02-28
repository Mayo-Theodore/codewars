import pytest
from array_diff import *

def test_integers_only():
    diff = ArrayDiff()
    assert diff.integers_only([1,3], ["1"]) == "List must only contain integers"

def test_maximum_list():
    diff = ArrayDiff()
    assert diff.check_length([1,3,3,1,3,5,1,3,6], [3,4]) == "List must contain a maximum of 5 integers"

def test_difference():
    diff = ArrayDiff()
    assert diff.difference([1,2], [1]) == [2]
    assert diff.difference([1,2], [1,3]) == [2]
    assert diff.difference([1,2], []) == [1,2]
    assert diff.difference([], [3,4]) == []
    assert diff.difference([1,2,2], [2]) == [1]


