#!/bin/python3

import sys


class babble_sort:
    def __init__(self, my_list):
        self.list = my_list

    def babble(self):
        count = 0
        for i in range(len(self.list)):
            for l in range(i, len(self.list)):
                if(self.list[i] > self.list[l]):
                    self.list[i], self.list[l] = self.list[l], self.list[i]
                    count += 1
        return count


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
my_class = babble_sort(a)
count = my_class.babble()
print("Array is sorted in {0} swaps.".format(count))
print("First Element: {}".format(my_class.list[0]))
print("Last Element: {}".format(my_class.list[-1]))
