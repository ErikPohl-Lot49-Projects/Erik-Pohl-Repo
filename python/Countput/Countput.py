'''
Created on Dec 14, 2018

@author: Erik Pohl
'''
from collections import Counter

class Countput(Counter):
    
 
    def return_list(self, n = None, delimiter = ' '):
        z= [delimiter.join([str(x) for x in i]) for i in self.most_common(n)]
        return z
        

    def output_topn(self, n = None, delimiter = ' '):
        [print(delimiter.join([str(x) for x in i])) for i in self.most_common(n)]        

