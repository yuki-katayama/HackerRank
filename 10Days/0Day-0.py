import statistics

a = int(input())
b=list(map(int,input().split()))
c = [0] * 1000000
d = []
for i in b:
    c[i] += 1
max_num = max(c)
for i, x in enumerate(c):
    if(x == max_num):
        d.append(i)
print(round(statistics.mean(b), 1))
print(round(statistics.median(b),1 ))
print(min(d))