from contextlib import contextmanager
from collections import defaultdict

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
            something_to_do_with_accepted_token=None
    ):
        self._turnstiles = []
        self._default_turnstile = None
        self.name = name
        self.value = value
        self.do_something_with_value = \
            something_to_do_with_my_value
        self.do_something_with_accepted_token = \
            something_to_do_with_accepted_token

    def add_turnstile(self, value, goto_node, fun=None ):
        try:
            iter(value) # TODO: note that a '"' shows as iterable -- is this okay?
        except:
            self._turnstiles.append(([value], (goto_node, fun)))
        else:
            self._turnstiles.append((value, (goto_node, fun)))

    def add_default_turnstile(self, goto_node, fun=None):
        self._default_turnstile = (goto_node, fun)

    def _execute_and_return(self, path, token ):
        if path[1]: # TODO : handle gracefully with namedtuple
            path[1](token)
        elif self.do_something_with_accepted_token:
            self.do_something_with_accepted_token(token)
        return path[0]

    def evaluate_token(self, token):
        if self.do_something_with_value:
            self.do_something_with_value(self.value)
        for turnstyle in self._turnstiles:
            if token in turnstyle[0]:
                return self._execute_and_return(turnstyle[1], token)
        if not self._default_turnstile:
            raise bad_token_exception
        return self._execute_and_return(self._default_turnstile, token)

    def consume_and_print_and_raise_exceptions(self, tokens):
        print('start', self.name)
        current_state = self
        for token in tokens:
            current_state = current_state.evaluate_token(token)
            if current_state is None:
                raise sequence_terminated_partially_consumed_exception
            print(token, current_state.name)

    def consume_and_print(self, tokens):
        print('start', self.name)
        current_state = self
        for token in tokens:
            current_state = current_state.evaluate_token(token)
            if current_state is None:
                break
            print("consumed {0} and went to {1}".format(
                str(token),
                current_state.name)
            )

    def is_consumed_completing_sequence_and_raising_exceptions(self, tokens):
        current_state = self
        for token in tokens:
            if current_state is None:
                raise sequence_terminated_partially_consumed_exception
            current_state = current_state.evaluate_token(token)
        raise (sequence_did_not_terminate_exception if current_state else True)

    def is_consumed_completing_sequence(self, tokens):
        current_state = self
        for token in tokens:
            if current_state is None:
                return False
            try:
                current_state = current_state.evaluate_token(token)
            except:
                return False
        return not current_state
