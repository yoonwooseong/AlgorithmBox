class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    # Add your code here

    def computeDifference(self):
        lists = []
        self.__elements.sort()
        for idx, val in enumerate(self.__elements):
            for j in range(idx, len(self.__elements)):
                lists.append(self.__elements[j] - val)
        self.maximumDifference = max(lists)

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
