import pytest
from duplicate_encoder import *

def test_ignore_capitalisation():
    assert capital("HeLLo") == "hello"

def test_return_brackets():
    assert brackets("HeLLo") == '((((('

def test_duplicate_chars():
    # assert duplicate_chars("din") == "((("
    # assert duplicate_chars("recede") == "()()()"
    # assert duplicate_chars("Success") == ")())())"
    # assert duplicate_chars("(( @") == "))((" 
    assert duplicate_chars("yO BHUSd") == '(((((((('

