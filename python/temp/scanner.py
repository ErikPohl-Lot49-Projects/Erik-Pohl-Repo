from json import loads, load
#from JnesaisQ import JnesaisQ, jnesaisq_compare

with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\the_modal_nodes.json','r') as f1:
    z = load(f1)

with open('C:\\Users\\p636205\\workspace\\jnesaisq\\JnesaisQ\\format.json','r') as f1:
    json_query_format = load(f1)

def scanner(xjson):
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
            if isinstance(xjson[i],dict) or isinstance(xjson[i],list):
                print(type(xjson[i]), xjson[i])
                print('calling')
                scanner(xjson[i])
            else:
                if (i == 'class') and (xjson[i] == 'Input'):
                    print(25*'*'+'Input') 
    return None

scanner(z)
