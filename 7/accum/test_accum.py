import pytest
from accum import *

def test_capitalize_letters():
    accum = Accum()
    assert accum.capitalize("RqaEzty") == "RQAEZTY"

def test_capitalize_and_add_hyphen():
    accum = Accum()
    assert accum.hyphen("RqaEzty") == "R-Q-A-E-Z-T-Y"

def test_accum():
    accum = Accum()
    assert accum.accum("abcd") == "A-Bb-Ccc-Dddd"
    assert accum.accum("cwAt") == "C-Ww-Aaa-Tttt"
    assert accum.accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    assert accum.accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
    assert accum.accum("Qsdoobuqinb") == 'Q-Ss-Ddd-Oooo-Ooooo-Bbbbbb-Uuuuuuu-Qqqqqqqq-Iiiiiiiii-Nnnnnnnnnn-Bbbbbbbbbbb'
    assert accum.accum("Kurgikmkphy") == 'K-Uu-Rrr-Gggg-Iiiii-Kkkkkk-Mmmmmmm-Kkkkkkkk-Ppppppppp-Hhhhhhhhhh-Yyyyyyyyyyy'



    





