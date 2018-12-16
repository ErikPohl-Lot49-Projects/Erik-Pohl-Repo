# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 13, 2018

@author: Erik Pohl
'''

from contextlib import contextmanager

# TODO: make this play nicely with countput and jnesaisq


@contextmanager
def xlate_to_string(
        xlate_input_delimiter,
        xlate_input_format=None,
        xlate_output_format=None
):
    xlate_instance = xlate(
        xlate_input_delimiter,
        xlate_input_format=xlate_input_format,
        xlate_output_format=xlate_output_format
    )
    if xlate_input_format:
        yield_fun = xlate_instance.to_string_using_keyword_format
    else:
        yield_fun = xlate_instance.to_string_forcing_positional
    yield yield_fun
    yield_fun = None


class xlate:
    '''easily xlate one string format into another
    string format -- using keywords or positional
    -- or even into a dictionary'''

    def __init__(
            self,
            xlate_input_delimiter,
            xlate_input_format=None,
            xlate_output_format=None
    ):
        self.input_delimiter = xlate_input_delimiter
        self.input_format = xlate_input_format
        self.output_format = xlate_output_format

    def _convert_to_positional(self, key_field_output_format):
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
                positional_output_format += key_field_output_format[
                                            last_index:first_index + 1
                                            ] + str(counter)
                counter += 1
                last_index = char_index
                first_index = None
        positional_output_format += key_field_output_format[last_index:]
        return positional_output_format

    def to_string_forcing_positional(self, input_data):
        '''
        takes an input, splits it by delimiter,
        applies a list of columns in the input_format,
        and returns fields in a string based on the output_format
        works on positional and non positional output
        '''
        return (
            self._convert_to_positional(self.output_format).format(
                *input_data.split(self.input_delimiter)
            )
        )

    def to_string_using_keyword_format(self, input_data):
        '''
        takes an input, splits it by delimiter,
        applies a list of columns in the input_format,
        and returns fields in a string based on the output_format
        works on positional and non positional output
        '''
        if self.input_format:
            return self.output_format.format(**self.to_dictionary(input_data))
        else:
            return (
                self.output_format.format(
                    *input_data.split(
                        self.input_delimiter
                    )
                )
            )

    def to_dictionary(self, input_data):
        '''
        takes an input, splits it by delimiter,
        applies a list of columns in the input_format
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
                        str(field_position) for field_position, _ in enumerate(
                            input_data.split(self.input_delimiter)
                        )
                    ],
                input_data.split(self.input_delimiter)
            )
        }
