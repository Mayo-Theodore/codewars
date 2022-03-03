import pytest
from camel_case import *

def test_camel_case():
    assert to_camel_case("the-stealth-warrior") == "theStealthWarrior"
    assert to_camel_case('The_Stealth_Warrior') == "TheStealthWarrior"
    # assert to_camel_case('A_cat-is-Omoshiroi') == 'ACatIsOmoshiroi'
