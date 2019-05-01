#!/usr/bin/env python

'''
Provides a function to convert roman numerals to arabic
without integer math
'''

from itertools import groupby

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Code Review"


def sneaky_roman_numerals(roman):
    '''
    translates roman numerals to arabic
    without using handy integer math
    '''
    
    base_ten_arabic_digit_places = {
        'M': 0,
        'C': 1,
        'X': 2,
        'I': 3
    }
    
    subtractive_phrases_and_factors = [('IV',4), 
                                       ('IX',9), 
                                       ('XL',4),
                                       ('XC',9), 
                                       ('CD',4), 
                                       ('CM',9)
                                       ]

    
    five_times_replace_numerals = [
        ('D', 'C'),
        ('V', 'I'),
        ('L', 'X')
    ]
    
    arabic = ['0','0','0','0']
    
    #roman = roman.upper()  # assumes uppercase
    
    if set(roman).difference({'I', 'V', 'X', 'L', 'C', 'D', 'M'}):
        raise ValueError;
    
    '''
    first, replace any subtractive phrase by its first letter.  
    Do it by the number of factors indicated for the phrase
    IV becomes IIII, both are 4
    ''' 
    for subtractive_phrase_and_factor in subtractive_phrases_and_factors:
        roman = roman.replace(subtractive_phrase_and_factor[0], 
                              subtractive_phrase_and_factor[0][0]*subtractive_phrase_and_factor[1]
                              )
    '''
    next, replace any five times letter with its replacement   
    Do it 5 times
    V becomes IIIII, both are 5
    ''' 
    for five_times_replace_numeral in five_times_replace_numerals:
        roman = roman.replace(five_times_replace_numeral[0], 5*five_times_replace_numeral[1])
    
    '''
    now that you have reduced it to numerals which can be summed
    group them
    and take their length as their sum
    in the corresponding arabic numeral place
    III is in place 3 and the length is 3
    so the number is 0003
    '''
    roman_numeral_groups = groupby(roman)
    for index,roman_numeral_group in roman_numeral_groups:
        arabic[base_ten_arabic_digit_places[index]] = str(len(list(roman_numeral_group)))
    return int(''.join(arabic))
        

if __name__ == '__main__':
    sneaky_roman_numerals('iii')
