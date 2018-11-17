import copy
import dill
from functools import wraps
import logging, sys


class deawkwardize:
    


    def __init__(self, fname):
        self.deawkdict = {}
        self.token = 0
        self.tokendict = {}
        self.deawkdictdelimiter = '||'
        try:
            with open(fname, 'r') as awkfile:
                for fline in awkfile:
                    a, b = fline.split(self.deawkdictdelimiter)
                    self.deawkdict[a] = b
        except Exception as e:
            print(e)



    def deawk(self, infname, outfname='deawked_', tokenfile = 'deawkdict.txt'):
        def gentoken(linex):
            #recognize dups with a dict

            try:
                return self.tokendict[linex]
            except:
                self.token += 1
                self.tokendict[linex] = self.token
                return (str(self.token))

        outfname = outfname + infname
        with open(infname, 'r') as deawk_input, open(outfname,"w") as deawk_output, \
            open(tokenfile,'w') as tokenfilehandle:
            for line in deawk_input:
                #find logging and comments and translate spitting translation into output file

                if line.strip().startswith('logging'):
                    newtoken = '#%'+ str(gentoken(line.strip()))
                    deawk_output.write(line.replace(line.strip(),newtoken) + '\n')
                    tokenfilehandle.write(newtoken + self.deawkdictdelimiter + line.strip()+'\n')
                    continue
                if line.strip().startswith('#'):
                    newtoken = '#@' + str(gentoken(line.strip()))
                    deawk_output.write(line.replace(line.strip(), newtoken)+ '\n')
                    tokenfilehandle.write(newtoken + self.deawkdictdelimiter + line.strip()+'\n')
                    continue
                deawk_output.write(line)

    def reawk_fileput(self, fname):
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

    def reawk_logging(self, *argsx):
        """"this is a decorator to guarantee specific keyword arguments are used
        in an otherwise open ended keyword argument list
        Allows for extra messaging and handling for an error related to missing or invalid keyword arguments
        """

        def real_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                testSource = dill.source.getsource(func)
                ## do replacement here for logging

                testSourceLines = testSource.split('\n')
                newtestinnersource = 'import logging, sys\nlogging.basicConfig(stream=sys.stdout, level=logging.INFO)\n'
                for line in testSourceLines:
                    if line.strip().startswith('#'):
                        try: #% only, though
                            replace = self.deawkdict[line.strip()]
                            newtestinnersource += replace + "\n"
                            continue
                        except:
                            replace = line.strip()
                        newtestinnersource += replace.strip() + '\n'
                    elif not line.strip().startswith('def') and not line.strip().startswith('@'):
                        newtestinnersource+=line.strip() +'\n'
                #print("new innersource\n", newtestinnersource)
                code_obj = compile(newtestinnersource, '<string>', 'exec')
                func.__code__ = copy.deepcopy(code_obj)
                result = func(*args, **kwargs)
                return result

            return wrapper
            func

        return real_decorator


da = deawkwardize('deawkdict.txt')


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
logging.info("hello")

logging.info("hello")

#print("REAWKING")
#da.reawk_fileput('DeAwkwardize.py')
