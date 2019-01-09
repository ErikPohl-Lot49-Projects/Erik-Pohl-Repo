import time
from operator import itemgetter
from itertools import repeat
from multiprocessing import Pool


class numerous_ants:

    def __init__(self, control_widget, ants, inputs, iterations):
        self.control_widget = control_widget
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
        start = time.time()
        for _ in repeat(None, iterations):
            output = function(*args)
        end = time.time()
        return (output, end - start)

    def log_result(self, result_value):
        pass

    def formicate(self):
        self.results = []
        pool = Pool()
        for this_ant in self.ants:
            total_time = 0
            for this_input in self.inputs:
                control_result = self.perform(
                    1,
                    self.control_widget,
                    this_input
                )
                experimental_result = pool.apply_async(
                    self.perform,
                    args=(
                        self.iterations,
                        this_ant[1],
                        this_input,
                    ),
                    callback=self.log_result
                ).get()
                if experimental_result[0] == control_result[0]:
                    total_time += experimental_result[1]
                else:
                    total_time = -1  # this is a problem
                    break
            self.results.append(total_time)

    def resultput(self):
        result_tuples = [
            (
                self.ants[result_counter][0],
                self.results[result_counter],
                self.results[result_counter] / sum(self.results) * 100
            )
            for result_counter, result
            in enumerate(self.results)
        ]
        for result_tuple in sorted(result_tuples, key=itemgetter(1)):
            print(result_tuple)
