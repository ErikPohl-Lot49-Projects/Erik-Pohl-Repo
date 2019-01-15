from itertools import groupby

def plural_rn(roman):
    
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
    
    for subtractive_phrase_and_factor in subtractive_phrases_and_factors:
        roman = roman.replace(subtractive_phrase_and_factor[0], 
                              subtractive_phrase_and_factor[0][0]*subtractive_phrase_and_factor[1]
                              )

    for five_times_replace_numeral in five_times_replace_numerals:
        roman = roman.replace(five_times_replace_numeral[0], 5*five_times_replace_numeral[1])
    
    roman_numeral_groups = groupby(roman)
    for index,roman_numeral_group in roman_numeral_groups:
        arabic[base_ten_arabic_digit_places[index]] = str(len(list(roman_numeral_group)))
    return int(''.join(arabic))
        
