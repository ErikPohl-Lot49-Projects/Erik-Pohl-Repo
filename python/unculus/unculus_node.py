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


class bad_token_exception(Exception):
    pass


class sequence_terminated_partially_consumed_exception(Exception):
    pass


class sequence_did_not_terminate_exception(Exception):
    pass


class unculus_node:

    def __init__(
            self,
            name,
            value=None,
            something_to_do_with_my_value=None,
            something_to_do_with_entrance_token=None
    ):
        self._options = []
        self.name = name
        self.value = value
        self.do_something_with_value = \
            something_to_do_with_my_value
        self.do_something_with_entrance_token = \
            something_to_do_with_entrance_token

    def add_option(self, goto_node, list_of_values):
        self._options.append((goto_node, {list_of_values}))

    def eval_val(self, val):
        if self.do_something_with_entrance_token:
            self.do_something_with_entrance_token(val)
        if self.do_something_with_value:
            self.do_something_with_value(self.value)
        for i in self._options:
            if val in i[1]:
                return i[0]
        raise bad_token_exception

    def consume_exceptions(self, l):
        print('start', self.name)
        start = self
        for i in l:
            start = start.eval_val(i)
            if start is None:
                raise sequence_terminated_partially_consumed_exception
            print(i, start.name)

    def consume(self, l):
        print('start', self.name)
        start = self
        for i in l:
            print("consuming token " + str(i))
            start = start.eval_val(i)
            if start is None:
                break
            print(i, start.name)

    def is_consumed_completing_sequence_exceptions(self, l):
        start = self
        for i in l:
            if start is None:
                raise sequence_terminated_partially_consumed_exception
            start = start.eval_val(i)
        raise (sequence_did_not_terminate_exception if start else True)

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
