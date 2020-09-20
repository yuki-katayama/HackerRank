class Difference:
    def __init__(self, a):
        self._elements = a

    def computeDifference(self):
        max = 0
        for i, num in enumerate(self._elements):
            for j in range(i + 1):
                comp = num - self._elements[j]
                if(comp < 0):
                    comp *= -1
                if(max < comp):
                    max = comp
        self.maximumDifference = max


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
print(d._elements)
d.computeDifference()

print(d.maximumDifference)
