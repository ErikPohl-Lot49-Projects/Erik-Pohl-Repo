# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2018

@author: Erik Pohl
'''

from xlate import xlate_string_formats

input_del = ' '
input_format = ['lname', 'fname', 'bdate', 'language_of_choice', 'hometown']
output_format = '{fname} {lname}, born on {bdate}, ' \
                'lives in {hometown} and prefers {language_of_choice}'

with xlate_string_formats(
        xlate_input_delimiter=input_del,
        xlate_output_format=output_format
) as f:
    input_string = 'pohl erik 9/2/72 python arlington'
    print(f(input_string))
    input_string = 'pynchon thomas 5/5/45 muted_posthorn manhattan'
    print(f(input_string))

with xlate_string_formats(
        xlate_input_delimiter=input_del,
        xlate_input_format=input_format,
        xlate_output_format=output_format
) as f:
    input_string = 'pohl erik 9/2/72 python arlington'
    print(f(input_string))
    input_string = 'pynchon thomas 5/5/45 muted_posthorn manhattan'
    print(f(input_string))
