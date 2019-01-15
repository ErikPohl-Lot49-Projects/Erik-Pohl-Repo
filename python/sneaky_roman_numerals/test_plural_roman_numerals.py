import pytest
from plural_roman_numerals import plural_roman_numerals

def test_null_case():
    assert plural_roman_numerals.plural_rn('') == 0
    
def test_simple_case():
    assert plural_roman_numerals.plural_rn('MCXIII') == 1113

def test_additive_case():
    assert plural_roman_numerals.plural_rn('MCLXVIII') == 1168
    assert plural_roman_numerals.plural_rn('MMDCCLXVIII') == 2768

def test_subtractive_case():
    assert plural_roman_numerals.plural_rn('IX') == 9
    assert plural_roman_numerals.plural_rn('XCIX') == 99
    assert plural_roman_numerals.plural_rn('CMXC') == 990
    assert plural_roman_numerals.plural_rn('CMXCIX') == 999
    assert plural_roman_numerals.plural_rn('CMXCIV') == 994
    assert plural_roman_numerals.plural_rn('CMXLIX') == 949
    assert plural_roman_numerals.plural_rn('CMXLIV') == 944
    assert plural_roman_numerals.plural_rn('CDXCIX') == 499
    assert plural_roman_numerals.plural_rn('CDXCIV') == 494
    assert plural_roman_numerals.plural_rn('CDXLIX') == 449
    assert plural_roman_numerals.plural_rn('CDXLIV') == 444
    
def test_longer_than_four_digits():
    assert plural_roman_numerals.plural_rn('MMMMMMMMMM') == 10000
    
