# !/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

# TODO potentially Guarantee will use regex on variable values for validation


def guarantee(*argsx):
    """"this is a decorator to guarantee specific keyword arguments are used
    in an otherwise open ended keyword argument list
    Allows for extra messaging and handling for an error
    related to missing or invalid keyword arguments
    """
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if list(argsx) != list(kwargs.keys()) and kwargs != {}:
                print(
                    "expected argument list [%s] "
                    "does not match argument list [%s]" % (
                        argsx, list(kwargs.keys()
                                    )
                    )
                )
                raise Exception("expected argument does not match argument")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return real_decorator
