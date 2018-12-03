# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"


# TODO: on sunday make this output messages
# https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9
#
class Error(Exception):
    """Base class for other exceptions"""

class UnrecognizedURLTestCase(Error):
    """Raised when a mocked API call function uses an unknown endpoint"""
    def __init__(self, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = 'this was an unrecognized test case!'
        print(msg)
