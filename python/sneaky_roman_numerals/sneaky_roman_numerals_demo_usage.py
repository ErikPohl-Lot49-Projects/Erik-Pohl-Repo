#!/usr/bin/env python

'''
Demo use cases for sneaky roman numerals
'''

from sneaky_roman_numerals import sneaky_roman_numerals

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Code Review"


def demo_sneaky_roman_numerals():
    '''
    Execute a number of edge and regression cases
    with output
    '''
    demo_cases = [
        ('', 0),
        ('MCXIII', 1113),
        ('MCLXVIII',1168),
        ('MMDCCLXXVIII',2778),
        ('MMMMMMMMMM',10000),
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
    ]
    for demo_case in demo_cases:
        print('For input {0}: Expected {1} and got {2}'.format(demo_case[0], str(demo_case[1]), str(sneaky_roman_numerals(demo_case[0]))))

if __name__ == '__main__':
    demo_sneaky_roman_numerals()
