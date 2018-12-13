# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2018

@author: Erik Pohl
'''

class xlate:
    
    def __init__(self, xlate_input, xlate_delimiter, xlate_input_format):
        self.input = xlate_input
        self.input_delimiter = xlate_delimiter
        self.input_format = xlate_input_format


    def xlate_to_str(self, output_format):
        '''
        takes an input, splits it by delimiter, applies a list of columns in the input_format,
        and returns fields in a string based on the output_format
        works on positional and non positional output
        '''
        if self.input_format:
            return output_format.format(**self.xlate_to_dict())
        else:
            return (output_format.format(*self.input.split(self.input_delimiter)))
    
    def xlate_to_dict(self):
        '''
        takes an input, splits it by delimiter, applies a list of columns in the input_format
        or numbers if no input format,
        and returns fields in a dict
        '''
        return {
            k:v for (k,v) in zip(
                self.input_format if self.input_format else [
                    str(x) for x,_ in enumerate(
                        self.input.split(
                            self.input_delimiter
                            )
                        )
                    ]
                , self.input.split(
                    self.input_delimiter
                    )
                )
            }
