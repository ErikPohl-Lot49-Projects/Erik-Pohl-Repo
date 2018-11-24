from guarantee import guarantee

@guarantee('n')
def fibonacci_keywordarg_guarantee(**kwargs):
    """uses guarantee decorator to guarantee a particular variable name is used with keyword
    arguments passed into an open-ended keyword argument"""
    if kwargs['n'] in (0,1):
        return kwargs['n']
    return (fibonacci_keywordarg_guarantee(n=kwargs['n']-2) + fibonacci_keywordarg_guarantee(n=kwargs['n']-1))

def fibonacci_keywordarg_standard_mandatory(*, n):
    """standard methodology to force use of the n keyword argument"""
    if n in (0,1):
        return n
    return (fibonacci_keywordarg_standard_mandatory(n=n-2) + fibonacci_keywordarg_standard_mandatory(n=n-1))


print(fibonacci_keywordarg_guarantee(n=9))
print(fibonacci_keywordarg_standard_mandatory(n=9))
