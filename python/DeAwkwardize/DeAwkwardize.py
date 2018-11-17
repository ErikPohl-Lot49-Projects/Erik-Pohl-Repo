import copy
import dill
from functools import wraps
import logging, sys


class deawkwardize:

    def __init__(self):
        self.deawkdict = {}
        self.token = 0
        self.tokendict = {}
        self.deawkdictdelimiter = '||'
        self.logging_token_prefix = '#%'
        self.comment_token_prefix = '#@'

    def load_token_dict(self, fname):
        '''
        Accepts as input the name of a token dictionary file
        loads the tokens into a token dictionary
        :param fname: Token dictionary file name
        :return: True
        '''
        try:
            with open(fname, 'r') as awkfile:
                for fline in awkfile:
                    a, b = fline.split(self.deawkdictdelimiter)
                    self.deawkdict[a] = b
        except Exception as e:
            print(e)
        return True

    def deawk(self, infname, outfname='deawked_', tokenfile='deawkdict.txt'):
        '''
        Accepts as input a python program name to output, 
        replaces all the comments and logging messages in it with tokens
        and writes the abbreviated [deawkwardized] file to and outfile
        with the tokens to a token file
        :param infname: Input python program
        :param outfname: Output deawkwardized python program
        :param tokenfile: output token file
        :return: True
        '''

        def gentoken(linex):
            # recognize dups with a dict

            try:
                return self.tokendict[linex]
            except:
                self.token += 1
                self.tokendict[linex] = self.token
                return (str(self.token))

        outfname = outfname + infname
        with open(infname, 'r') as deawk_input, open(outfname, "w") as deawk_output, \
                open(tokenfile, 'w') as tokenfilehandle:
            for line in deawk_input:
                # find logging and comments and translate spitting translation into output file

                if line.strip().startswith('logging'):
                    newtoken = self.logging_token_prefix + str(gentoken(line.strip()))
                    deawk_output.write(line.replace(line.strip(), newtoken) + '\n')
                    tokenfilehandle.write(newtoken + self.deawkdictdelimiter + line.strip() + '\n')
                    continue
                if line.strip().startswith('#'):
                    newtoken = self.comment_token_prefix + str(gentoken(line.strip()))
                    deawk_output.write(line.replace(line.strip(), newtoken) + '\n')
                    tokenfilehandle.write(newtoken + self.deawkdictdelimiter + line.strip() + '\n')
                    continue
                deawk_output.write(line)
        return True

    def reawk_fileput(self, fname):
        '''
        This takes a token dictionary
        and restores a file to its awkward glory
        with comments and full logging messages
        replacing the abbreviated tokens
        :param fname: File name to output with comments and logging restored
        :return: True
        '''
        with open(fname, 'r') as deawk_file:
            for line in deawk_file:
                # translate lines into reawked lines and output

                if line.strip().startswith('#'):
                    try:
                        print(line.replace(line.strip(), self.deawkdict[line.strip()]))
                    except:
                        print(line)
                else:
                    print(line)
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
                testSource = dill.source.getsource(func)
                ## do replacement here for logging

                testSourceLines = testSource.split('\n')
                newtestinnersource = 'import logging, sys\nlogging.basicConfig(stream=sys.stdout, level=logging.INFO)\n'
                for line in testSourceLines:
                    if line.strip().startswith(self.logging_token_prefix):
                        try:  # % only, though
                            replace = self.deawkdict[line.strip()]
                            newtestinnersource += replace + "\n"
                            continue
                        except:
                            replace = line.strip()
                        newtestinnersource += replace.strip() + '\n'
                    elif not line.strip().startswith('def') and not line.strip().startswith('@'):
                        newtestinnersource += line.strip() + '\n'
                # print("new innersource\n", newtestinnersource)
                code_obj = compile(newtestinnersource, '<string>', 'exec')
                func.__code__ = copy.deepcopy(code_obj)
                result = func(*args, **kwargs)
                return result

            return wrapper
            func

        return real_decorator


da = deawkwardize()
da.load_token_dict('deawkdict.txt')


# Define a function we want to modify:

@da.reawk_logging()
def test():
    logging.info("hello")
    print("Here")


@da.reawk_logging('')
def test2():
    logging.info("hello")
    print("Hello world")


# Run the function to check output


# print('\n\nRunning Function...')

test()
# >>> Here


test2()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

##da.deawk('DeAwkwardize.py')
logging.info("hello3")

logging.info("hello4")

# print("REAWKING")
# da.reawk_fileput('DeAwkwardize.py')
