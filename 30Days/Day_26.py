from datetime import datetime
import math

sub = list(map(int, input().split()))
limit = list(map(int, input().split()))

date = datetime(sub[2], sub[1], sub[0])
date1 = datetime(limit[2], limit[1], limit[0])

deff = date - date1
deff = int(deff.days)
if(deff < 1):
    print(0)
elif(sub[2] != limit[2]):
    print(10000)
else:
    sum = 0
    if(deff / 32 >= 1):
        sum += 500 * (math.floor(deff / 32))
    else:
        sum += 15 * (deff % 32)
    print(sum)
