from setsy import setsy

x = setsy([(1, 2), (1, 3)])
b = setsy([6, 7, 8])
print(x.issubset(b))
print(x.issuperset(b))
x = x.union(b)  # class setsy which inherits from set returns a set from union
print(x)
print(type(x))
y = {6, 5, 2, 1}
print('------------')
print(x.cartesian(y))
