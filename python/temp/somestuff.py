def remdups(a):
    z = set(a)
    for i in z:
        while a.count(i) > 1:
            a.remove(i)
    return True
    
def remdups2(a):
    for i in a:
        while a.count(i) > 1:
            a.remove(i)
    return True
    
az = [1,1,1,1,3,3,3,3,2,2,2,2,5,6,7,8,8,8,9,10]
print(az)
remdups(az)
print(az)


az = [1,1,1,1,3,3,3,3,2,2,2,2,5,6,7,8,8,8,9,10]
print(az)
remdups(az)
print(az)
print(all(ax > 0 for ax in az))
print(all(ax > 2 for ax in az))
