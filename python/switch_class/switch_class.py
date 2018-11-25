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

    def add_switch_clause(self, switch_condition, switch_value, break_on_match):
        self.decision_clauses.append({'switch_condition': switch_condition,
                                      'result': switch_value,
                                      'break_on_match': break_on_match})

    def execute_switch(self, compare_value):
        retval = []
        for x in self.decision_clauses:
            switch_condition, result, break_on_match = x['switch_condition'], x['result'], x['break_on_match']
            if compare_value in switch_condition:
                retval.append(result)
                if break_on_match:
                    break
        return (retval if retval != [] else self.default_return_value)
