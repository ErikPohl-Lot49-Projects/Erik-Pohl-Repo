import inspect
import copy
from django.template.base import kwarg_re

s = frozenset([1,2,3])

a = 5
print(id(a))
b= a
print(id(a))

b+=1
print(id(b))

b = 6
print(id(b))

def foobar(arg = []):
    print(id(arg))
    arg[1] = 9
    print(id(arg))

    print(arg)

l = [1,2,3]
print(id(l))
foobar(l)
print(id(l))
print(l)


v = [1,2,3,[4,5]]
h = copy.copy(v)
h[3][0] = 5
print(v,h) 
n = copy.deepcopy(v)
n[3][0] = 4
print(v,n)


class mylist(list):

    
    ## cannot override x= y
    ## can override x[k] = y
    def __setitem__(self, *args, **kwargs):
        z = copy.deepcopy(self)
        return list.__setitem__(z, *args, **kwargs)
 
print('using mylist')   
v1 = mylist( [1,2,3,[4,5]])
v1 = [1,2,3,[4,5]]
h1 = copy.copy(v)
h1[3][0] = 5
print(v1,h1) 
n1 = copy.deepcopy(v1)
n1[3][0] = 5
print(v1,n1)
    
class mylist2(list):

    def __init__(self, *args,**kwargs ):
        self = copy.deepcopy(self)
 
print('using mylist')   
v1 = mylist( [1,2,3,[4,5]])
v1 = [1,2,3,[4,5]]
h1 = copy.copy(v)
h1[3][0] = 5
print(v1,h1) 
n1 = copy.deepcopy(v1)
n1[3][0] = 5
print(v1,n1)
    

print('using mylist2')   
v1 = mylist2( [1,2,3,[4,5]])
v1 = [1,2,3,[4,5]]
h1 = copy.copy(v)
h1[3][0] = 5
print(v1,h1) 
n1 = copy.deepcopy(v1)
n1[3][0] = 5
print(v1,n1)
    


maxx = 12
minn = 10
x = 11
if x > minn and x < maxx:
    print('hello')
if minn < x and x < maxx:
    print("hello")
if minn < x < maxx:
    print("hello")
if 1 < x:
    print("hello")


from functools import reduce

a = [1,2,3,4,5,6,7]
# Apply function of two arguments cumulatively to the items of sequence, 
# from left to right, so as to reduce the sequence to a single value. 
# For example, reduce(lambda x, y: x+y, 
# [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
b = reduce(lambda x,y: y if y>x else x,a)
print(a,'reduced',b)

#@functools.singledispatch

from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register
def fun(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)
        
@fun.register(complex)
def fun(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)

@fun.register(complex)
def fun(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)


## wraps
from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()


example.__name__

example.__doc__

