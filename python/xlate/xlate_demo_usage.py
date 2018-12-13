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
output_format = '{fname} {lname}, born on {bdate}, lives in {hometown} and prefers {language_of_choice}'

demo_usage = xlate(input_string, input_del, input_format)
print(demo_usage.xlate_to_str(output_format))
print(demo_usage.xlate_to_dict())

output_format = '{0} {1}, born on {2}, lives in {3} and prefers {4}'
demo_usage = xlate(input_string, input_del, None)
print(demo_usage.xlate_to_str(output_format))
print(demo_usage.xlate_to_dict())




