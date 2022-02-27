import pytest
from who_likes_it import *

def test_no_likes():
    assert likes([]) == "no one likes this"

def test_one_likes():
    assert likes(["John"]) == "John likes this"

def test_two_likes():
    assert likes(["John", "Jason"]) == "John and Jason like this"

def test_three_likes():
    assert likes(["John", "Jason", "Max"]) == "John, Jason and Max like this"

def test_multiple_likes():
    assert likes(["John", "Jason", "Max", "Oliver", "Giggs"]) == "John, Jason and 3 others like this"