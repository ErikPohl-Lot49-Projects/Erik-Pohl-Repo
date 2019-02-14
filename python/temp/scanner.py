from json import loads, load
#from JnesaisQ import JnesaisQ, jnesaisq_compare

with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\the_modal_nodes.json','r') as f1:
    z = load(f1)

with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\format.json','r') as f1:
    json_query_format = load(f1)

def scanner(xjson):
    recursable_tags = ('subviews', 'contentView', 'input', 'control')
    print('called;', type(xjson),xjson)
    if isinstance(xjson, str):
        print('string leaf')
        return None
    if isinstance(xjson, list):
        print('scanning list')
        for c,i in enumerate(xjson):
            print('recursing list item [ ' + str(c))
            scanner(i)
        return None
    if isinstance(xjson,dict): 
        print('indict')
        for i in xjson.keys():
            if isinstance(xjson[i],dict) or (i != 'classNames' and isinstance(xjson[i],list)):
                if i in recursable_tags:
                    print(type(xjson[i]), xjson[i])
                    print('calling')
                    scanner(xjson[i])
            else:
                if (i == 'class') and (xjson[i] == 'Input'):
                    print(25*'*'+i + ' : ' + xjson[i])
                if (i == 'identifier') and (xjson[i] == 'apply'):
                    print(25*'#'+i + ' : ' + xjson[i])
                if (i == 'classNames') and ('container' in xjson[i]):
                    print(25*'>'+i + ' : ' + ''.join(xjson[i])) 
    return None

scanner(z)
