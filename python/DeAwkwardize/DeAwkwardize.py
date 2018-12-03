# !/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import dill
from functools import wraps

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"

# TODO: Allow multiple lines of comments concurrent to roll up into one deawk
# TODO: Use #[tab] and more of them in sequence
# TODO: With a header # this code had been deawkwardized to represent comments
# TODO: And #[space] for logging
# TODO: And make header message not deawked
# TODO: https://en.wikipedia.org/wiki/Memoization
# TODO: refactor
# TODO: make delimiter logic better--
# TODO: what if a comment or code has the delimiter in it naturally?
# TODO: maybe use a database back-end
# TODO: maybe improve token generation logic to create more interesting tokens
# TODO: consider my concept of layering, as a developer
# TODO: works from pseudocode down-- so this could work with PyJamb
# TODO: address how to handle common or anticipated exceptions
# TODO: handle different types of logging messages
# TODO: than just explicit logging lines
# TODO: handle a case where a def is within a def when reawking logging!
# TODO: shorten function and variable names
# TODO: encrypt and then decrypt on the fly?
#  https://nitratine.net/blog/post/encryption-and-decryption-in-python/


class deawkwardize:
    '''
    Deawkwardize allows a user to
    deawkwardize a python program by splitting it into a file
    with tokens instead of comments/logging and a token file
    or reawkwardize it:
        reawk logging is a decorator which in real time
        replaces tokens with logging messages to restore logging
        reawk file output is a method which
        outputs a file in its original form with full comments and logging
    '''

    def __init__(self):
        self.reawk_token_dictionary = {}
        self.current_token_sequence_number = 0
        self.deawk_token_dictionary = {}
        self.deawkwardize_token_file_delimiter = '||'
        self.standard_reawk_function_code_header = \
            'import logging, sys\n' \
            'logging.basicConfig(stream=sys.stdout, level=logging.INFO)\n'
        self.logging_token_prefix = '#%'
        self.comment_token_prefix = '#@'
        self.logging_startswith = 'logging'
        self.comment_startswith = '#'
        self.token_translation = [
            {self.logging_startswith: self.logging_token_prefix},
            {self.comment_startswith: self.comment_token_prefix}
            ]

    def load_deawk_token_dictionary(self, deawk_token_file_name):
        '''
        Accepts as input the name of a token dictionary file
        loads the tokens into a token dictionary
        :param deawk_token_file_name: Token dictionary file name
        :return: True
        '''
        try:
            with open(deawk_token_file_name, 'r') as deawk_file_handle:
                for fline in deawk_file_handle:
                    a, b = fline.split(self.deawkwardize_token_file_delimiter)
                    self.reawk_token_dictionary[a] = b
        except Exception as e:
            print(e)
        return True

    def generate_deawk_token(self, code_line_to_generate_a_token_for):
        # recognize dups with a dict

        try:
            return self.deawk_token_dictionary[
                code_line_to_generate_a_token_for
            ]
        except:
            self.current_token_sequence_number += 1
            self.deawk_token_dictionary[
                code_line_to_generate_a_token_for
            ] = self.current_token_sequence_number
            return (str(self.current_token_sequence_number))

    def tokenize(self, line, prefix, deawk_output_handle, token_file_handle):
        newtoken = prefix + \
                   str(
                       self.generate_deawk_token(
                           line.strip()
                       )
                   )
        deawk_output_handle.write(
            line.replace(line.strip(),
                         newtoken) +
            '\n')
        token_file_handle.write(
            newtoken +
            self.deawkwardize_token_file_delimiter +
            line.strip() +
            '\n')
        return True

    def deawk(self,
              deawk_input_file_name,
              deawk_output_file_prefix='deawked_',
              deawk_token_file='deawkdict.txt'
              ):
        '''
        Accepts as input a python program name to output,
        replaces all the comments and logging messages in it with tokens
        and writes the abbreviated [deawkwardized] file to and outfile
        with the tokens to a token file
        :param deawk_input_file_name: Input python program
        :param deawk_output_file_prefix: Output deawkwardized
        python program
        :param deawk_token_file: output token file
        :return: True
        '''

        deawk_output_file_prefix = deawk_output_file_prefix +\
            deawk_input_file_name
        with open(deawk_input_file_name, 'r') as deawk_input_handle, \
                open(deawk_output_file_prefix, "w") as deawk_output_handle, \
                open(deawk_token_file, 'w') as token_file_handle:
            for line in deawk_input_handle:
                for starts_with in self.token_translation:
                    if line.strip().startswith(starts_with):
                        self.tokenize(line,
                                      self.token_translation[starts_with],
                                      deawk_output_handle,
                                      token_file_handle)
                        continue
                deawk_output_handle.write(line)
        return True

    def reawk_fileput(self, reawk_input_file_name):
        '''
        This takes a token dictionary
        and restores a file to its awkward glory
        with comments and full logging messages
        replacing the abbreviated tokens
        :param reawk_input_file_name: File name to output
        with comments and logging restored
        :return: True
        '''
        with open(reawk_input_file_name, 'r') \
                as reawk_file_handle:
            for reawk_file_line in reawk_file_handle:
                # translate lines into reawked lines and output

                if reawk_file_line.strip().startswith('#'):
                    try:
                        print(reawk_file_line.replace(
                            reawk_file_line.strip(),
                            self.reawk_token_dictionary[
                                reawk_file_line.strip()
                            ]))
                    except:
                        print(reawk_file_line)
                else:
                    print(reawk_file_line)
        return True

    def reawk_logging(self, *argsx):
        """"this decorater uses a token dictionary to
        replace during runtime
        certain tokens
        with full logging messages
        to allow logging without logging messages in
        the code
        NOTE: since this involves self-modifying editing of code in real time
        do not use this on programs which
        fly the space shuttle
        perform surgery on people
        etc.
        """

        def real_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                function_source_code = dill.source.getsource(func)
                # do replacement here for logging

                function_source_code_lines = \
                    function_source_code.split('\n')
                reawked_replacement_source_code = \
                    self.standard_reawk_function_code_header
                for function_source_line in function_source_code_lines:
                    if function_source_line.strip().startswith(
                            self.logging_token_prefix):
                        try:  # % only, though
                            reawk_code_line_replacement = \
                                self.reawk_token_dictionary[
                                    function_source_line.strip()
                                ]
                            reawked_replacement_source_code += \
                                reawk_code_line_replacement + "\n"
                            continue
                        except:
                            reawk_code_line_replacement = \
                                function_source_line.strip()
                        reawked_replacement_source_code += \
                            reawk_code_line_replacement.strip() + '\n'
                    elif not function_source_line.strip().startswith('def') \
                            and not \
                            function_source_line.strip().startswith('@'):
                        reawked_replacement_source_code \
                            += function_source_line.strip() + '\n'

                compiled_code_object = compile(reawked_replacement_source_code,
                                               '<string>', 'exec')
                func.__code__ = copy.deepcopy(compiled_code_object)
                reawked_code_return_value = func(*args, **kwargs)
                return reawked_code_return_value

            return wrapper
            func
        return real_decorator
