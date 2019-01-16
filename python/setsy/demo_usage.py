from setsy import setsy


x = setsy([(1, 2), (1, 3)])
b = setsy([6, 7, 8])
print('here' , list(b.powerset()))
print(x.issubset(b))
print(x.issuperset(b))
x = x.union(b)  # class setsy which inherits from set returns a set from union
print(x)
print(type(x))
y = {6, 5, 2, 1}
print('------------')
print(x.cartesian(y))

print("is not subset attempt")
a = setsy([1,2,3])
print("a:", a)
b = setsy([2,3,4,5,6,7])
print("b:", b)
c = a.is_not_subset(b)
print("result of a.is_not_subset(b): ", c)
if c:
    print("a is not a subset of b")

print("is not superset attempt")
a = setsy([1,2,3])
print("a:", a)
b = setsy([2,3,4,5,6,7])
print("b:", b)
c = b.is_not_superset(a)
print("result of b.is_not_superset(a): ", c)
if c:
    print("b is not a superset of a")

print("is not subset attempt")
a = setsy([2,3])
print("a:", a)
b = setsy([2,3,4,5,6,7])
print("b:", b)
c = a.is_not_subset(b)
print("result of a.is_not_subset(b): ", c)
print("a is not a subset of b") if c else print("a is a subset of b")

print("is not superset attempt")
a = setsy([2,3])
print("a:", a)
b = setsy([2,3,4,5,6,7])
print("b:", b)
c = b.is_not_superset(a)
print("result of b.is_not_superset(a): ", c)
if c:
    print("b is not a superset of a")

print("is not subset attempt")
a = setsy([2,3])
print("a:", a)
b = setsy([2])
print("b:", b)
c = a.is_not_subset(b)
print("result of a.is_not_subset(b): ", c)
print("a is not a subset of b") if c else print("a is a subset of b")

print("is not superset attempt")
a = setsy([2,3])
print("a:", a)
b = setsy([2])
print("b:", b)
c = b.is_not_superset(a)
print("result of b.is_not_superset(a): ", c)
if c:
    print("b is not a superset of a")





