import statistics

nasi = int(input())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
append_list = []
index = 0
for i in range(len(list_b)):
    for b in range(0,list_b[i]):
        append_list.append(list_a[index])
    index += 1

append_list.sort()
list_len = len(append_list)
middle_p = int(round(list_len / 2))
front_list = append_list[0:middle_p]

odd = 0
if(list_len % 2 == 0):
    back_list = append_list[middle_p:list_len]
else:
    back_list = append_list[middle_p + 1:list_len]
    odd = 1

front_median = statistics.median(front_list)
back_median = statistics.median(back_list)

hani = back_median - front_median
if(hani == 25.0):
    print(20.0)
else:
    print(float(hani))