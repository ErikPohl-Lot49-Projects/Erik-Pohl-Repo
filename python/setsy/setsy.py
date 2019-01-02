class setsy(set):

    def __init__(self, n):
        self.iter = n
        super(setsy, self).__init__(n)

    def difference(self, n):
        return setsy(self.copy().difference(n))

    def symmetric_difference(self, n):
        return setsy(self.copy().symmetric_difference(n))

    def intersection(self, n):
        return setsy(self.copy().intersection(n))

    def union(self, n):
        return setsy(self.copy().union(n))

    def __str__(self):
        return '{' + ''.join([str(x)+', ' for x in self.iter])[:-2] + '}'

    def printorig(self):
        print(self.iter)

    def cartesian(self, b):
        d = []
        for i in self.iter:
            for j in b:
                d.append((i, j))
        return setsy(d)

    def power(self):
        for i in range(len(self.copy())+1):
            if i  == 0:
                print(setsy([]))
            if i == 1:
                for j in self.copy():
                    print(j)
            if i == 2:
                z = self.cartesian(self.copy())
                print(z)
            if i ==3 :
                z = self.cartesian(self.copy()).cartesian(self.copy())
                print(z)