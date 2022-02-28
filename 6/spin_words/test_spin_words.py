import pytest
from spin_words import *

def test_word_split():
    assert word_split("hello") == ["hello"]
    assert word_split("hello there") == ["hello", "there"]

def test_word_count():
    assert word_count("hello") == [5]
    assert word_count("hello you") == [5, 3]

def test_spin_a_word():
    assert spin_a_word("hello") == "olleh"

def test_spin_words():
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This is a test") == "This is a test"
    assert spin_words("This is another test") == "This is rehtona test"


