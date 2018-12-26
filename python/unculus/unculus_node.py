from contextlib import contextmanager

''''@contextmanager
def switch_compare(
        switch_default, switch_list
):
    switch_instance = unculus_node(
        switch_default
    )
    for i in switch_list:
        switch_instance.add_switch_clause(*i)
    yield_fun = switch_instance.execute_switch
    yield yield_fun
    yield_fun = None
'''

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
        raise ValueError

    def consume(self,l):
        print('start', self.name)
        start = self
        for i in l:
            try:
                start = start.eval_val(i)
            except:
                break
            if start is None:
                break
            print(i, start.name)

    def is_consumed_completing_sequence(self, l):
        start = self
        for i in l:
            if start is None:
                return False
            try:
                start = start.eval_val(i)
            except:
                return False
        return not start







