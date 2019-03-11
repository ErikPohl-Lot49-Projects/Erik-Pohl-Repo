


class kleene():
    '''
    common regex usage translation
    '''
    
    def __init__(self):
        pass
    
    def list_of_values(self, list):
        '''
        returns regex expression for list of values
        '''
        return '^(' + ''.join(['\\b'+str(y)+'|' for x,y in enumerate(list) if x != len(list)]) + ')'+'{1}'+'$'

if __name__ == '__main__':
    k = kleene()
    z = [1,2,3,4,5]
    patternstr = k.list_of_values(z)
    print('pattern ' + patternstr)
    import re
    f = re.search(patternstr, '3')
    print(f)
    z = ['Hello', 'Goodbye', 'Aloha']
    patternstr = k.list_of_values(z)
    print('pattern ' + patternstr)
    import re
    f = re.search(patternstr, '3')
    print(f)
        
        
