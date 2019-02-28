# !/usr/bin/env python
# -*- coding: utf-8 -*-
from guarantee import guarantee_regex, guarantee_variable_names

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"


def visual_delimiter(title=None):
    print('-'*80)
    if title:
        print(title)
        print('-'*80)
        
    
@guarantee_regex({'n':'.*'})
def fibonacci_keywordarg_guarantee(**kwargs):
    """uses guarantee decorator to guarantee a particular
    variable name is used with keyword
    arguments passed into an open-ended keyword argument"""
    nput = kwargs['n']
    if nput in (0, 1):
        return nput
    return (
            fibonacci_keywordarg_guarantee(
                n=nput-2
            ) +
            fibonacci_keywordarg_guarantee(
                n=nput-1
            )
    )


def fibonacci_keywordarg_standard_mandatory(*, n):
    """standard methodology to force use of the n keyword argument"""
    if n in (0, 1):
        return n
    return (
            fibonacci_keywordarg_standard_mandatory(n=n-2) +
            fibonacci_keywordarg_standard_mandatory(n=n-1)
    )

@guarantee_variable_names({'n':'.*'},{'x':'.*'})
def printout_guarantee(**kwargs):
    """uses guarantee decorator to guarantee a particular
    variable name is used with keyword
    arguments passed into an open-ended keyword argument"""
    print(kwargs['n'], kwargs['x'])


@guarantee_regex({'n':'5'},{'x':'hello'})
def printout_specific_guarantee(**kwargs):
    """uses guarantee decorator to guarantee a particular
    variable name is used with keyword
    arguments passed into an open-ended keyword argument"""
    print(kwargs['n'], kwargs['x'])

if __name__ == '__main__':
    visual_delimiter('Basic arg check for N using guarantee')
    print(fibonacci_keywordarg_guarantee(n=9))
    visual_delimiter('Standard argument check for mandatory keyword arguments without guarantee')
    print(fibonacci_keywordarg_standard_mandatory(n=9))
    visual_delimiter('Gurantee two arguments with their values [both wildcards]')
    printout_guarantee(n = 1, x= 2)
    visual_delimiter('Fail because I am only supplying one argument using guarantee for two arguments and values')
    try:
        printout_guarantee(n=1)
    except:
        print("it worked! an exception was generated")
    visual_delimiter('now try with a argument value problem for x')
    try:
        printout_specific_guarantee(n=5, x = 'goodbye')
    except:
        print('guarantee regex worked! an exception was generated')
    visual_delimiter('now try with a argument value problem for n')
    try:
        printout_specific_guarantee(n=2, x = 'hello')
    except:
        print('guarantee regex worked! an exception was generated')
    visual_delimiter('now try with no argument value problems')
    try:
        printout_specific_guarantee(n=5, x = 'hello')
        print('guarantee regex worked! no exception was generated')
    except:
        print('guarantee regex failed! an exception was generated')
    try:
        printout_specific_guarantee(z=5, x = 'hello')
        print('guarantee regex failed! no exception was generated')
    except:
        print('guarantee regex worked! an exception was generated')
    visual_delimiter()
    
