import time
from operator import itemgetter
from itertools import repeat
from multiprocessing import Pool

class numerous_ants:

    def __init__(self, control_widget, widgets , inputs, iterations):
        self.control_widget = control_widget
        self.widgets = widgets
        self.iterations = iterations
        self.results = []
        self.inputs = inputs

    def perform(self,its, fun, *args):
        start = time.time()
        for _ in range(its):
            z = fun(*args)
        end = time.time()
        return (z, end-start)
    
    def log_result(self,z):
        pass

    def formicate(self):
        self.results = []
        pool = Pool()
        for i in self.widgets:
            totaltime = 0
            for k in self.inputs:
                control_val = self.perform(1, self.control_widget,k)
                z = pool.apply_async(
                    self.perform, args = (self.iterations,i[1], k,), callback = self.log_result).get()
                if z[0] == control_val[0]:
                    totaltime += z[1]
                else:
                    totaltime = -1 ## this is a problem
                    break
            self.results.append(totaltime)


    def resultput(self):
        l = [(self.widgets[i][0], self.results[i], self.results[i]/sum(self.results)*100) for i,j in enumerate(self.results)]
        for j in sorted(l, key=itemgetter(1)):
            print(j)
