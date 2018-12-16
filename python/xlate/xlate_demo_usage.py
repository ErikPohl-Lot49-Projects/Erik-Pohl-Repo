# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2018

@author: Erik Pohl
'''

from xlate import xlate

input_string = 'pohl erik 9/2/72 python arlington'
input_del = ' '
input_format = ['lname', 'fname', 'bdate', 'language_of_choice', 'hometown']
output_format = '{fname} {lname}, born on {bdate}, ' \
                'lives in {hometown} and prefers {language_of_choice}'
demo_usage = xlate(
    xlate_input_delimiter=input_del,
    xlate_input_format=input_format,
    xlate_output_format=output_format
)

print(demo_usage.to_string_using_keyword_format(input_string))
print(demo_usage.to_dictionary(input_string))

output_format = '{0} {1}, born on {2}, lives in {3} and prefers {4}'
demo_usage = xlate(
    xlate_input_delimiter=input_del,
    xlate_output_format=output_format
)
print(demo_usage.to_string_using_keyword_format(input_string))
print(demo_usage.to_dictionary(input_string))

output_format = '{fname} {lname}, born on {bdate}, ' \
                'lives in {hometown} and prefers {language_of_choice}'
demo_usage = xlate(
    xlate_input_delimiter=input_del,
    xlate_output_format=output_format
)
print(demo_usage.to_string_forcing_positional(input_string))
