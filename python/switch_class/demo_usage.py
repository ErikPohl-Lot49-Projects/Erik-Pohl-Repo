# !/usr/bin/env python
# -*- coding: utf-8 -*-
from switch_class import switch

def foo():
    return ['1','2']

my_switch = switch('Not found')
my_switch.add_switch_clause('2', 'Two',False)
my_switch.add_switch_clause(['2','3'], 'Three',False)
my_switch.add_switch_clause(foo(), 'X',False)
my_switch.add_switch_clause('4', 'Four',True)
my_switch.add_switch_clause('4', 'Should not get here',True)
print(my_switch.execute_switch('1'))
print(my_switch.execute_switch('2'))
print(my_switch.execute_switch('5'))
print(my_switch.execute_switch('4'))
