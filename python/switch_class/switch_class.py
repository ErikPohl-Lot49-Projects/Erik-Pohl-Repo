# !/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager


@contextmanager
def switch_compare(
        switch_default, switch_list
):
    switch_instance = switch(
        switch_default
    )
    for i in switch_list:
        switch_instance.add_switch_clause(*i)
    yield_fun = switch_instance.execute_switch
    yield yield_fun
    yield_fun = None


class switch:
    '''
    Damn the torpedoes (https://www.python.org/dev/peps/pep-3103/),
    I'm implementing a switch class.
    In doing so, I inevitably join about a billion
    other people who did the same
    who also miss this from their C programming
    days.
    '''

    def __init__(self, default_return_value):
        self.default_return_value = default_return_value
        self.decision_clauses = []

    def __repr__(self):
        z = 'Switch statement in order of evaluation:\n'
        for i in self.decision_clauses:
            z = z + "on {switch_condition} return {result} and break on match: ({break_on_match})\n".format(**i)
        z = z + "default value: " + str(self.default_return_value)
        return z

    def add_switch_clause(self, switch_condition, switch_result, break_on_match):
        '''
        add, in sequence of switching, a switch logic clause with condition,
        result, and brake instruction
        :param switch_condition: The condition for which the switch result will fire
        :param switch_result: The switch result for a given condition
        :param break_on_match: Halt further switch evaluation on match?
        :return: True
        '''
        self.decision_clauses.append({'switch_condition': switch_condition,
                                      'result': switch_result,
                                      'break_on_match': break_on_match})
        return True

    def execute_switch(self, compare_value):
        '''
        execute_switch
        send a compare value through the switch to determine any results
        from the switch logic
        :param compare_value: this is a value to be compared against switch logic
        :return: any results the compare value provoked in the switch logic
        '''
        retval = []
        for decision_clause in self.decision_clauses:
            switch_condition, \
            result, \
            break_on_match = decision_clause['switch_condition'], \
                             decision_clause['result'], \
                             decision_clause['break_on_match']
            if compare_value in switch_condition:
                retval.append(result)
                if break_on_match:
                    break
        return (retval if retval != [] else self.default_return_value)
