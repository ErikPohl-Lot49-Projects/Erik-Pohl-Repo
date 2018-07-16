class freqdict:
    countdict = {}
    pctdict = {}
    def __init__(self, evalstring):
        countdict = {}
        pctdict = {}
        sum = 0
        for i in evalstring:
            sum=sum+1
            if i in countdict.keys():
                countdict[i] += 1
            else:
                countdict[i] = 1
        for i in countdict.keys():
            pctdict[i] = float(countdict[i]/sum)
        self.countdict =countdict
        self.pctdict = pctdict
    def getmin(self):
        minloc = -1
        minval = -1
        for i in self.pctdict.keys():
            if (minloc == -1) or ((self.pctdict[i] < minval) and self.pctdict[i] != -1):
                minloc = i
                minval = self.pctdict[i]
        self.pctdict[minloc] = -1
        return minloc, minval
    def allzero(self):
        for i in self.pctdict.keys():
            if self.pctdict[i] != -1:
                return False
        return True

class node:
    def __init__(self, inputvalue, inputindex, freqc, lchild =-1, rchild =-1):
        self.value = int(inputvalue)
        self.indx = int(inputindex)
        self.freq = float(freqc)
        self.lchild = lchild
        self.rchild=rchild
        self.leaf = 1

class huffman:
    maxindx = 0
    seeddict = {}
    name =0
    def incindx(self):
        self.maxindx +=1
    def __init__(self, evalstring):
        self.tree = []
        self.indx =0
        self.seeddict = freqdict(evalstring)
        for x in self.seeddict.pctdict.keys():
            print('adding freq', self.seeddict.pctdict[x])
            print('adding value', x)
            print('adding index', self.maxindx)
            n = node(x, self.maxindx, self.seeddict.pctdict[x])
            self.tree.append(n)
            self.incindx()
    def getindex(self, lkpval):
        for i in self.tree:
            if int(i.value) == lkpval:
                return i.indx
        return -1
    def hasparent(self,ind):
        #print("checking ind for parent", ind)
        for i in self.tree:
            #print(i.rchild,i.lchild)
            if int(i.rchild) == ind or int(i.lchild) == ind:
                #print('yes')
                return True
        return False
    def getmin(self):
        minval = 1000.0 # fix this
        minloc = 1000
        #print('get min')
        #print('here')
        for i in self.tree:
            #print('current min',minval)
            #print('comparing against',i.freq)
            if   (not self.hasparent(i.indx)) and (i.freq < minval):
                #print("changing min from ",minval,i.freq)
                minval = i.freq
                minloc = i.indx
        #print("returning loc",minloc)
        if minloc == 1000:
            minloc =-1
        return minval, minloc
    def printtree(self):
        print('printtree')
        for i in self.tree:
            print(i.indx, i.lchild, i.rchild, i.freq,  i.value, )
    def oneorphans(self):
        x=0
        for i in self.tree:
            print(i.indx,self.hasparent((i.indx)))
            if not self.hasparent(i.indx):
                x=x+1
        return x
    def blockout(self,pindx):
        for i in self.tree:
            if i.indx == pindx:
                i.freq = 1000.0
    def setrightchild(self,dinx,rchild,val):
        for i in self.tree:
            if i.indx == dinx:
                i.rchild = rchild
                i.freq=val


if __name__ == '__main__':
    a = huffman('1123')
    mv =1.0
    mv2 = 1.0
    ml2 = 1
    for i in a.seeddict.pctdict.keys():
        print(i,a.seeddict.pctdict[i])
    print('dumptree')
    for i in a.tree:
        print(i.freq,i.value,i.indx,i.lchild, i.rchild)
    print(a.getindex(2))
    print("peeling off")
    while not a.seeddict.allzero():
        z,x= a.seeddict.getmin()
        print(z,x)
    a.printtree()
    counter = 0
    while not a.oneorphans()==1 and counter < 7:
        print('here', a.oneorphans())
        mv,ml = a.getmin()
        print('index before',a.maxindx)
        a.incindx()
        print('index after',a.maxindx)
        n = a.tree.append(node(3, a.maxindx, 4.0, ml, 0))
        mv2,ml2 = a.getmin()
        if ml2 == a.maxindx:
            mv2=0.0
        else:
            a.setrightchild(a.maxindx,ml2,mv+mv2)
        counter +=1

        #a.blockout(ml)
    a.printtree()







