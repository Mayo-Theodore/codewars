import pytest
from phone_number import *

def test_check_is_array():
    create_phone = CreatePhone()
    assert create_phone.check_number(["a, b, c"]) == "Not a valid phone number"
    assert create_phone.check_number([1, 2, 3]) == "Valid phone number"


def test_check_length():
    create_phone = CreatePhone()
    assert create_phone.check_length([3]) == "Insufficient digits"
    assert create_phone.check_length([3, 1, 2, 3, 1, 5, 5, 5, 1, 1]) == "Sufficient digits"

def test_convert_list_to_str():
    create_phone = CreatePhone()
    create_phone.convert([3, 1, 2, 3, 1, 5, 5, 5, 1, 1]) == '3123155511'

def test_first_three_digits():
    create_phone = CreatePhone()
    assert create_phone.first_digits([3, 1, 2, 3, 1, 5, 5, 5, 1, 1]) == '(312)3155511'

def test_create_number():
    create_phone = CreatePhone()
    assert create_phone.create_number([3, 1, 2, 3, 1, 5, 5, 5, 1, 1]) == '(312) 315-5511'


    