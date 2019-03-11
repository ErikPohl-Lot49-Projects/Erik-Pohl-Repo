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
        #/^(foo|bar){1}$/
        extra = '{1}'
        result = '\/^(' + ''.join([str(y)+'|' for x,y in enumerate(list) if x != len(list)-1])+str(list[len(list)-1]) + ')' + extra + '$\/'
        result = '^(' + ''.join(['\\b'+str(x)+'|' for x,y in enumerate(list) if x != len(list)])+'\\b'+str(list[len(list)-1]) + ')'+extra+'$'
        return result
