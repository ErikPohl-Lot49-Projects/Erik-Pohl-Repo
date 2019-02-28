# !/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import re

# TODO: can this be combined into one?
# TODO: regex assumes string or byte types-- so won't work for various inputs
# TODO: type checking of input variables?
# TODO: support function validation (lambda and otherwise)

def guarantee_regex(*argsx):
    """"this checks the values of the arguments
    and the names of the arguments
    """
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #print(argsx,kwargs)
            try:
                # attempt 1, regex and key value match at same time
                if not all([re.match(str(list(argument.values())[0]),str(kwargs[next(iter(argument))])) for argument in argsx]):
                    raise ValueError
            except:
                print(
                    "expected argument list [%s] "
                    "does not match argument list [%s]" % (
                        argsx, list(kwargs.items()
                                    )
                    )
                )
                raise Exception("expected argument does not match argument")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return real_decorator

def guarantee_variable_names(*argsx):
    """"this is a decorator to guarantee specific keyword arguments are used
    in an otherwise open ended keyword argument list
    Allows for extra messaging and handling for an error
    related to missing or invalid keyword arguments
    """
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #print(argsx,kwargs)
            try:
                [kwargs[next(iter(argument))] for argument in argsx]
            except:
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
