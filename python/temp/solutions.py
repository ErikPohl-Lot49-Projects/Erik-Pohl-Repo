That is a ridiculous statement. There was NO Android 20 years ago. There was no Google Photos 20 years ago. There was NO YouTube 20 years ago. There was no TPUs 20 years ago. There was no Angular, or Flutter or Fuchsia or Zircon or Google Maps or Google WifI or Google Homes or Google inventing GANS or Capsule networks or AlphaGo or Google Chrome or well the list goes on and on.


class Solution:
    def twoSum(self, nums, target):
        j = min(nums)
        if j < 0:
            offset = -j
        else:
            offset = 0
        z = sorted([(n,v+offset) for (n,v) in list(enumerate(nums)) if v <=target+offset*2],key=lambda z: z[1])
        from itertools import combinations
        for i in combinations(z,2):
            x1 = tuple(i)[0]
            x2 = tuple(i)[1]
            if x1[1] + x2[1] == target+offset*2:
                return [x1[0], x2[0]]
        return [0,0]
        
class Solution:
    def isPalindrome(self, x):
        n = list(str(x))
        for i,v in enumerate(n):
            if v != n[len(n)-i-1]:
                return False
        return True
		
class Solution:
    def longestCommonPrefix(self, strs):
        common = ""
        if len(strs) > 0:
            a = min(len(i) for i in strs)
            for j in range(a):
                v = strs[0]
                for n in strs:
                    if n[j] != v[j]:
                        return common
                common += v[j]
        return common
        
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        if len(nums) > 0:
            ln = max(nums)+1
            while i < len(nums):
                print(nums[i], ln)
                if nums[i] == ln:
                    del nums[i]
                else:
                    ln= nums[i]
                    i=i+1              
        return len(nums)
		
from copy import copy
def recurse(prices, ind=0):
    def indprint(x,*a):
        print(''.join([' ' for i in range(x)]), a)
              
    def pricetrim(prlist):
        if len(prlist) <=0:
            return
        while prlist[0] == max(prlist):
            del prlist[0]
            if len(prlist) <=0:
                return

    maxval = 0
    pr = copy(prices)
    pricetrim(pr)
    indprint(ind,pr)
    for i,j in enumerate(pr):
        for k in range(i+1,len(pr)):
            value = 0    
            prx = copy(pr)
            indprint(ind, 'using indices ' + str(i) +   ' ' + str(k))
            indprint(ind, 'which is '+ str(pr[i]) +' ' + str(pr[k]))
            indprint(ind, 'resulting in :'+ str(pr[k]-pr[i]))
            for n2 in range(k,-1,-1): # was i-1 instead of 0
                indprint(ind, 'index deletion ' + str(n2))
                del prx[n2]
                indprint(ind,prx)
            indprint(ind,'recursing')
            value = value + pr[k]-pr[i] + recurse( prx, ind+3)
            indprint(ind,"value: "+ str(value))
            if value > maxval:
                maxval = value
                indprint(ind,'maxval is now = '+ str(maxval))
    return maxval    
            
    
a = [7,1,5,3,6,4] #7
a = [1,2,3,4,5] #4
a= [7,6,4,3,1] #0
print(recurse(a))

#print(recurse(a))   

# time limit exceeded
class Solution:
    def maxProfit(self, prices):
        def pricetrim(prlist):
            if len(prlist) <=0:
                return
            while prlist[0] == max(prlist):
                del prlist[0]
                if len(prlist) <=0:
                    return
        from copy import copy
        maxval = 0
        pr = copy(prices)
        pricetrim(pr)
        for i,j in enumerate(pr):
            for k in range(i+1,len(pr)):
			
                value = 0    
                if pr[k] > pr[i]:
                    prx = copy(pr)
                    for n2 in range(k,-1,-1): # was i-1 instead of 0
                        del prx[n2]
                    value = value + pr[k]-pr[i] + self.maxProfit( prx)
                    if value > maxval:
                        maxval = value
        return maxval
