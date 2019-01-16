from itertools import chain, combinations


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
        return '{' + ''.join([str(element) + ', ' for element in set(self.iter)])[:-2] + '}'

    def printorig(self):
        print(self.iter)

    def cartesian(self, multiply_by):
        resultset = []
        for level in self.iter:
            for element in multiply_by:
                resultset.append((level, element))
        return setsy(resultset)

    def powerset(self):
        setsy_set = self.copy()
        return setsy(list(
            chain.from_iterable(
                combinations(
                    setsy_set,
                    length_of_combo
                )
                for length_of_combo in range(len(setsy_set) + 1
                                             )
            )
        )
        )

    def is_not_subset(self, c):
        setsy_set = self.copy()
        return setsy(setsy_set.difference(c))

    def is_not_superset(self, c):
        setsy_set = self.copy()
        setsy_set_parameter = setsy(c)
        return setsy(setsy_set_parameter.difference(setsy_set))


