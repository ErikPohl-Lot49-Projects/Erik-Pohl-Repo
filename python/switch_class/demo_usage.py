# !/usr/bin/env python
# -*- coding: utf-8 -*-
from switch_class import switch, switch_compare

def foo():
    return ['1','2']

my_switch = switch('Not found')
my_switch.add_switch_clause('2', 'Two',False)
my_switch.add_switch_clause(['2','3'], 'Three',False)
my_switch.add_switch_clause(foo(), 'X',False)
my_switch.add_switch_clause('4', 'Four',True)
my_switch.add_switch_clause('4', 'Should not get here',True)
my_switch.add_switch_clause({'6':1}, 'Six',True)
print(my_switch.execute_switch('1'))
print(my_switch.execute_switch('2'))
print(my_switch.execute_switch('5'))
print(my_switch.execute_switch('4'))
print(my_switch.execute_switch('6'))

print(my_switch)


with switch_compare(
    'Not found', 
    [
        ('2', 'Two',False), 
        (['2','3'], 'Three',False), 
        (foo(), 'X',False), 
        ('4', 'Four',True), 
        ('4', 'Should not get here',True),
        ({'6':1}, 'Six', True)
        ]
    ) as x:
    print(x('1'))
    print(x('2'))
    print(x('5'))
    print(x('4'))
    print(x('6'))
