from itertools import groupby

def plural_rn(roman):
    
    arabic_digit_places = {
        'M': 0,
        'C': 1,
        'X': 2,
        'I': 3
    }
    
    subtractive_phrases = ['IV', 'IX', 'XL','XC', 'CD', 'CM']
    
    five_times_replace_numerals = [
        ('D', 'C'),
        ('V', 'I'),
        ('L', 'X')
    ]
    
    subtractive_replace_factor = {
            'V': 4,
            'X': 9,
            'L': 4,
            'C': 9,
            'D': 4,
            'M': 9}
  
    arabic = ['0','0','0','0']
    
    for subtractive_phrase in subtractive_phrases:
        roman = roman.replace(subtractive_phrase, 
                              subtractive_phrase[0]*subtractive_replace_factor[
                                  subtractive_phrase[1]
                                  ]
                              )

    for five_times_replace_numeral in five_times_replace_numerals:
        roman = roman.replace(five_times_replace_numeral[0], 5*five_times_replace_numeral[1])
    
    process_roman = groupby(roman)
    for i,j in process_roman:
        arabic[arabic_digit_places[i]] = str(len(list(j)))
    return int(''.join(arabic))
        
