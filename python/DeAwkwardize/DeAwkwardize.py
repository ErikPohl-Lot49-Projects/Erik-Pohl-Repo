import copy
from functools import wraps

import dill


# TODO: https://en.wikipedia.org/wiki/Memoization
# TODO: refactor
# TODO: make delimiter logic better--
# what if a comment or code has the delimiter in it naturally?
# TODO: maybe use a database back-end
# TODO: maybe improve token generation logic to create more interesting tokens
# TODO: consider my concept of layering, as a developer
# works from pseudocode down-- so this could work with PyJamb
# TODO: address how to handle common or anticipated exceptions
# TODO: handle different types of logging messages
# than just explicit logging lines
# TODO: shorten function and variable names
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
        self.reawkwardize_token_dictionary = {}
        self.current_token_sequence_number = 0
        self.deawkwardize_token_dictionary = {}
        self.deawkwardize_token_file_delimiter = '||'
        self.standard_reawk_function_code_header = \
            'import logging, sys\n' \
            'logging.basicConfig(stream=sys.stdout, level=logging.INFO)\n'
        self.logging_token_prefix = '#%'
        self.comment_token_prefix = '#@'

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
                    self.reawkwardize_token_dictionary[a] = b
        except Exception as e:
            print(e)
        return True

    def deawk(self,
              deawkwardize_input_file_name,
              deawkwardize_output_file_name='deawked_',
              deawkwardize_token_file='deawkdict.txt'
              ):
        '''
        Accepts as input a python program name to output,
        replaces all the comments and logging messages in it with tokens
        and writes the abbreviated [deawkwardized] file to and outfile
        with the tokens to a token file
        :param deawkwardize_input_file_name: Input python program
        :param deawkwardize_output_file_name: Output deawkwardized
        python program
        :param deawkwardize_token_file: output token file
        :return: True
        '''

        def generate_deawkwardize_token(code_line_to_generate_a_token_for):
            # recognize dups with a dict

            try:
                return self.deawkwardize_token_dictionary[
                    code_line_to_generate_a_token_for
                ]
            except:
                self.current_token_sequence_number += 1
                self.deawkwardize_token_dictionary[
                    code_line_to_generate_a_token_for
                ] = self.current_token_sequence_number
                return (str(self.current_token_sequence_number))

        deawkwardize_output_file_name = \
            deawkwardize_output_file_name + deawkwardize_input_file_name
        with open(deawkwardize_input_file_name, 'r') as deawk_input, \
                open(deawkwardize_output_file_name, "w") as deawk_output, \
                open(deawkwardize_token_file, 'w') as tokenfilehandle:
            for line in deawk_input:
                # find logging and comments and translate spitting translation
                # into output file

                if line.strip().startswith('logging'):
                    newtoken = self.logging_token_prefix + \
                               str(
                                   generate_deawkwardize_token(
                                       line.strip()
                                   )
                               )
                    deawk_output.write(
                        line.replace(line.strip(),
                                     newtoken) +
                        '\n')
                    tokenfilehandle.write(
                        newtoken +
                        self.deawkwardize_token_file_delimiter +
                        line.strip() +
                        '\n')
                    continue
                if line.strip().startswith('#'):
                    newtoken = self.comment_token_prefix + \
                               str(generate_deawkwardize_token(line.strip()))
                    deawk_output.write(
                        line.replace(line.strip(), newtoken) +
                        '\n'
                    )
                    tokenfilehandle.write(
                        newtoken + self.deawkwardize_token_file_delimiter +
                        line.strip() +
                        '\n'
                    )
                    continue
                deawk_output.write(line)
        return True

    def reawk_fileput(self, reawkwardize_input_file_name):
        '''
        This takes a token dictionary
        and restores a file to its awkward glory
        with comments and full logging messages
        replacing the abbreviated tokens
        :param reawkwardize_input_file_name: File name to output
        with comments and logging restored
        :return: True
        '''
        with open(reawkwardize_input_file_name, 'r') \
                as reawkwardize_file_handle:
            for reawkwardize_file_line in reawkwardize_file_handle:
                # translate lines into reawked lines and output

                if reawkwardize_file_line.strip().startswith('#'):
                    try:
                        print(reawkwardize_file_line.replace(
                            reawkwardize_file_line.strip(),
                            self.reawkwardize_token_dictionary[
                                reawkwardize_file_line.strip()
                            ]))
                    except:
                        print(reawkwardize_file_line)
                else:
                    print(reawkwardize_file_line)
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
                                self.reawkwardize_token_dictionary[
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

                # print("new innersource\n", newtestinnersource)

                compiled_code_object = compile(reawked_replacement_source_code,
                                               '<string>', 'exec')

                func.__code__ = copy.deepcopy(compiled_code_object)
                reawked_code_return_value = func(*args, **kwargs)
                return reawked_code_return_value

            return wrapper
            func

        return real_decorator
