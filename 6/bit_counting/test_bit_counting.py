import pytest
from bit_counting import *

def test_return_binary():
    assert convert_to_binary(1234) == 10011010010

def test_count_binary():
    assert count_binary(1234) == 5