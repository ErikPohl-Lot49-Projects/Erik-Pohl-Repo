import pytest
from plural_roman_numerals import plural_roman_numerals

def test_simple_case():
    assert plural_roman_numerals.plural_rn('MCXIII') == 1113

def test_addition_case():
    assert plural_roman_numerals.plural_rn('MCLXVIII') == 1168
    
def test_subtraction_case():
    assert plural_roman_numerals.plural_rn('IX') == 9
    assert plural_roman_numerals.plural_rn('XCIX') == 99
    assert plural_roman_numerals.plural_rn('MMMMMMMMMM') == 10000


 
    
