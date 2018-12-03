#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
from DeAwkwardize import deawkwardize

# DEMO USAGE CODE

da = deawkwardize()
da.load_deawk_token_dictionary('deawkdict.txt')


# Define a function we want to modify:

@da.reawk_logging()
def foo():
    '''
    the #%11 gets translated at runtime to a logging message
    of hello by reawk_logging
    :return:
    '''
    # %11
    print("obligatory foo")


@da.reawk_logging('')
def bar():
    '''
    the #%11 gets translated at runtime to a logging message of hello
    by reawk_logging
    :return:
    '''
    # %11
    print("obligatory bar")


# Run the function to check output

# print('\n\nRunning Function...')

foo()
# >>> Here

bar()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# da.deawk('DeAwkwardize.py')

# print("REAWKING")
# da.reawk_fileput('DeAwkwardize.py')

logging.info("This is an awkward logging message")
logging.info("so is this")
