import pytest
from plural_roman_numerals import plural_roman_numerals


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
    assert plural_roman_numerals.plural_rn(roman_input) == expected_arabic
