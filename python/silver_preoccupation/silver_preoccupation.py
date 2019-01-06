import time
from operator import itemgetter


class silver_preoccupation:

    def __init__(self, widgets , iterations):
        self.widgets = widgets
        self.iterations = iterations
        self.results = []

    def perform(self,fun, *args):
        fun(*args)

    def first_call(self):
        self.results = []
        for i in self.widgets:
            start = time.time()
            for j in range(self.iterations):
                self.perform(i[1], i[2])
            end = time.time()
            self.results.append(end-start)

    def resultput(self):
        l = [(self.widgets[i][0], self.results[i], self.results[i]/sum(self.results)*100) for i,j in enumerate(self.results)]
        for j in sorted(l, key=itemgetter(1)):
            print(j)




