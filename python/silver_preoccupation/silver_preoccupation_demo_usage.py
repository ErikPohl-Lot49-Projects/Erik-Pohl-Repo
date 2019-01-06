from silver_preoccupation import silver_preoccupation

answer = 'x'


def trial1(answer):
        if not (answer == 'yes' or answer == 'no'):
            pass

def trial2(answer):
        if answer not in ('yes', 'no'):
            pass

def trial3(answer):
        if answer not in ['yes', 'no']:
            pass

def trial4(answer):
        if answer not in {'yes', 'no'}:
            pass

def trial5(answer):
    if answer in {'yes'} or answer in { 'no'}:
        pass

def trial6(answer):
    if {'yes','no'}.issuperset({answer}):
        pass

l = [('trial1',trial1, answer), ('trial2',trial2,answer), ('trial3',trial3,answer), ('trial4',trial4,answer),
     ('trial5', trial5, answer), ('trial6', trial6, answer)]
x = silver_preoccupation(l, 20000000)
x.first_call()
x.resultput()
