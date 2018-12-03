# !/usr/bin/env python
# -*- coding: utf-8 -*-
from guarantee import guarantee

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"


@guarantee('n')
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

print(
    fibonacci_keywordarg_guarantee(n=9)
)
print(
    fibonacci_keywordarg_standard_mandatory(n=9)
)
