import time
from operator import itemgetter


class silver_preoccupation:

    def __init__(self, control_widget, widgets , inputs, iterations):
        self.control_widget = control_widget
        self.widgets = widgets
        self.iterations = iterations
        self.results = []
        self.inputs = inputs

    def perform(self,fun, *args):
        return fun(*args)

    def first_call(self):
        self.results = []
        totaltime = 0
        for i in self.widgets:
            for k in self.inputs:
                start = time.time()
                for j in range(self.iterations):
                    z = self.perform(i[1],k)
                end = time.time()
                if z ==self.perform(self.control_widget,k):
                    totaltime += end-start
                else:
                    totaltime = 0
                    break
            self.results.append(totaltime)


    def resultput(self):
        l = [(self.widgets[i][0], self.results[i], self.results[i]/sum(self.results)*100) for i,j in enumerate(self.results)]
        for j in sorted(l, key=itemgetter(1)):
            print(j)




