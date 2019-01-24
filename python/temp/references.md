https://pymotw.com/3/inspect/index.html


import inspect
import copy

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
        return list.__setitem__(self, *args, **kwargs)
    
