class unculus_node:

    def __init__(self,name):
        self._options = []
        self.name = name

    def add_option(self, goto_node, list_of_values):
        self._options.append((goto_node, {list_of_values}))

    def eval_val(self, val):
        for i in self._options:
            if val in i[1]:
                return i[0]

    def consume(self,l):
        print('start', self.name)
        start = self
        for i in l:
            start = start.eval_val(i)
            if start is None:
                break
            print(i, start.name)







