from base64 import decode
import pytest
from morse import *

def test_translate():
    # assert decoder('·-') == 'A'
    # assert decoder('.- .-') == 'AA'
    # assert decodeMorse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE'
    assert decodeMorse('...---...') == 'SOS'
