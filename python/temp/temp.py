class asterisks():
    def __enter__(self):
        print('*' * 32)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('*' * 32)

with asterisks():
    print("hello")
    
class dunderchange():
    def __enter__(self):
        print("here")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("there")
    
with dunderchange():
    x= 0
    x = x + 1
    x = x + 3
    print(x)

from contextlib import ContextDecorator, contextmanager

@contextmanager
def addonenote():
    
    def addto(x):
        x[0]+=1
        return x
    print("enter")
    x = [0]
    addto(x)
    addto(x)
    yield addto(x)
    print("exit")

with addonenote() as z:
    print("yo" + str(z))
    print("yo" + str(z))
    print("yo" + str(z))    
    print("yo" + str(z))
    print("yo" + str(z))
    print("yo" + str(z))



def change(x):
    x[0] = x[0]+1

x = [1]
change(x)
change(x)
change(x)
change(x)
change(x)
change(x)
print("changed x")
print(x)
class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting') 
        return self


    def __exit__(self, *exc):
        print('Finishing')
        return False
    
@mycontext()
def function():
    print("This is the middle")

function()
