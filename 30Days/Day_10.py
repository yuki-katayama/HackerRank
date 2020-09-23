a = bin(int(input()))
b = a[3:]
count = 1
mem = a[2]
mem_list = []
for i, param in enumerate(b):
    if(mem == b[i]):
        count += 1
    else:
        count = 1
    mem = b[i]
    mem_list.append(count)

print(max(mem_list))
