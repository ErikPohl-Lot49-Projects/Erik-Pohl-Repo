import time
from operator import itemgetter
from itertools import repeat
from multiprocessing import Pool
from contextlib import redirect_stdout
import io

class numerous_ants:
    '''Compare a list of functions asynchronously to find the fastest
    one which behaves exactly like one designated the control (the queen)'''

    def __init__(self, queen, ants, inputs, iterations):
        self.queen = queen
        self.ants = ants
        self.iterations = iterations
        self.results = []
        self.inputs = inputs

    def perform(
            self,
            iterations,
            function,
            *args
    ):
        '''Execute a function for a number of iterations with given arguments'''
        redirect_here = io.StringIO()
        with redirect_stdout(redirect_here):
            start = time.time()
            for _ in repeat(None, iterations):
                    output = function(*args)
            end = time.time()
        return (output, end - start)

    def log_result(self, result_value):
        '''log result currently does nothing, but could later track results'''
        pass

    def formicate(self):
        '''for a series of algorithms run them asynchronously
        for a series of inputs--
        get rid of any which do not behave the same as the queen 
        (a control algorithm) and time the runtime of the rest
        to find the fastest'''
        self.results = []
        control_results = {this_input:self.perform(
                    1,
                    self.queen,
                    this_input
                )[0]
            for this_input in self.inputs
            }
        pool = Pool()
        for this_ant in self.ants:
            total_time = 0
            for this_input in self.inputs:    
                experimental_result = pool.apply_async(
                    self.perform,
                    args=(
                        self.iterations,
                        this_ant[1],
                        this_input,
                    ),
                    callback=self.log_result
                ).get()
                if experimental_result[0] == control_results[this_input]:
                    total_time += experimental_result[1]
                else:
                    total_time = -1  # this is a problem
                    break
            self.results.append(total_time)

    def resultput(self):
        '''output the results of an anthill formication'''
        result_tuples = [
            (
                self.ants[result_counter][0],
                self.results[result_counter],
                self.results[result_counter] / sum(self.results) * 100
            )
            for result_counter, _
            in enumerate(self.results)
        ]
        for result_tuple in sorted(result_tuples, key=itemgetter(1)):
            print(result_tuple)
