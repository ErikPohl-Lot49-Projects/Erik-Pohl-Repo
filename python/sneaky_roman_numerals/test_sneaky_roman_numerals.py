#!/usr/bin/env python

'''
Regression test cases for sneaky roman numerals
'''

import pytest
from sneaky_roman_numerals import sneaky_roman_numerals

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Code Review"


@pytest.mark.parametrize("roman_input,expected_arabic", [
## null case
    ('', 0),
## simple case
    ('MCXIII', 1113),
## additive cases
    ('MCLXVIII',1168),
    ('MMDCCLXXVIII',2778),
## longer than four digits in Arabic
    ('MMMMMMMMMM',10000),
## subtractive cases
    ('IX', 9),
    ('XCIX', 99),
    ('CMXC', 990),
    ('CMXCIX', 999),
    ('CMXCIV', 994),
    ('CMXLIX', 949),
    ('CMXLIV', 944),
    ('CDXCIX', 499),
    ('CDXCIV', 494),
    ('CDXLIX', 449),
    ('CDXLIV', 444)
])
def test_roman_to_arabic(roman_input, expected_arabic):
    assert sneaky_roman_numerals.sneaky_roman_numerals(roman_input) == expected_arabic

def test_roman_to_arabic_error():
    try:
        assert sneaky_roman_numerals.sneaky_roman_numerals('ZIII') == 10
        raise AssertionError
    except ValueError:
        print("Expected error")
    try:
        assert sneaky_roman_numerals.sneaky_roman_numerals('iii') == 3
        raise AssertionError
    except ValueError:
        print("Expected error")
    
