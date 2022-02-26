import pytest
from unique_in_order import *

def test_unique():
    assert unique('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    assert unique('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']

    assert unique([1,2,2,3,3]) == [1,2,3]
    assert unique([]) == []
    assert unique(['A']) == ['A']



