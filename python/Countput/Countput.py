'''
Created on Dec 14, 2018

@author: Erik Pohl
'''
from collections import Counter, OrderedDict
import sys
import re
from wsgiref.simple_server import sys_version

class Countput(Counter):
    
    def mycmp(self,version1, version2):
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
        return normalize(version1) >=  normalize(version2) 
    
 
    def return_list(self, n = None, delimiter = ' '):
        z= [delimiter.join([str(x) for x in i]) for i in self.most_common(n)]
        return z
        

    def output_topn(self, n = None, delimiter = ' '):
        [print(delimiter.join([str(x) for x in i])) for i in self.most_common(n)]        

    def return_dict(self):
        # do something different for versions of Python
        # where the dictionary is not automatically ordered
        if self.mycmp('.'.join((str(sys.version_info.major),str(sys.version_info.minor), str(sys.version_info.micro))),"3.7.1"):
            return_dictionary = {}
        else:  
            return_dictionary = OrderedDict()   
        return_dictionary.update({frequency_tuple[0]:frequency_tuple[1] for frequency_tuple in self.most_common()})
        return return_dictionary
