# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

nasi = int(input())

a = list(map(int, input().split()))
a.sort()

a_length = len(a)
middle_num = round(a_length / 2)

if(a_length % 2 == 0):
    middle = (a[middle_num] + a[middle_num - 1]) / 2
    c = middle_num
else:
    middle = a[round(middle_num)]
    c = middle_num + 1

b = statistics.median(a[0:middle_num])
c = statistics.median(a[c:a_length])
print(int(b),int(middle),int(c),sep="\n")
