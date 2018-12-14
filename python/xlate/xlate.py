# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2018

@author: Erik Pohl
'''


class xlate:

    def __init__(self, xlate_input, xlate_delimiter, xlate_input_format=None):
        self.input = xlate_input
        self.input_delimiter = xlate_delimiter
        self._input_list = self.input.split(self.input_delimiter)
        self.input_format = xlate_input_format

    def convert_to_positional(self, key_field_output_format):
        '''
        converts an output format into positional from field names
        :param key_field_output_format: output format
        :return:
        '''
        positional_output_format = ''
        first_index = None
        last_index = 0
        counter = 0
        for char_index, character in enumerate(key_field_output_format):
            if character == '{':
                first_index = char_index
            if character == '}' and first_index is not None:
                positional_output_format += key_field_output_format[last_index:first_index + 1] + str(counter)
                counter += 1
                last_index = char_index
                first_index = None
        positional_output_format += key_field_output_format[last_index:]
        return positional_output_format

    def to_string_forcing_positional(self, output_format):
        '''
        takes an input, splits it by delimiter, applies a list of columns in the input_format,
        and returns fields in a string based on the output_format
        works on positional and non positional output
        '''
        return (self.convert_to_positional(output_format).format(*self._input_list))

    def to_string_using_keyword_format(self, output_format):
        '''
        takes an input, splits it by delimiter, applies a list of columns in the input_format,
        and returns fields in a string based on the output_format
        works on positional and non positional output
        '''
        if self.input_format:
            return output_format.format(**self.to_dictionary())
        else:
            return (output_format.format(*self._input_list))

    def to_dictionary(self):
        '''
        takes an input, splits it by delimiter, applies a list of columns in the input_format
        or numbers if no input format,
        and returns fields in a dict
        '''
        return {
            key: value
            for (key, value)
            in zip(
            self.input_format
            if self.input_format
            else [
                str(field_position)
                for field_position, _
                in enumerate(
                    self._input_list
                )
            ],
            self._input_list)
        }
