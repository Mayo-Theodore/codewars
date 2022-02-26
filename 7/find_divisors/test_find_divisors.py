import pytest
from find_divisors import *

def test_integer_greater_than_1():
    divisors = Divisors()
    assert divisors.is_greater(1) == "Integer must be greater than 1"
    assert divisors.is_greater(3) == "Integer is greater than 1"

def test_divisible_by():
    divisors = Divisors()
    assert divisors.divisible_by(15) == [3, 5]
    assert divisors.divisible_by(24) == [2,3,4,6,8,12]
    assert divisors.divisible_by(25) == [5]
    assert divisors.divisible_by(253) == [11, 23]
    assert divisors.divisible_by(3734) == [2, 1867]


def test_is_prime():
    divisors = Divisors()
    assert divisors.is_prime(3) == "3 is prime"
    assert divisors.is_prime(17) == "17 is prime"
    assert divisors.is_prime(29) == "29 is prime"



    

