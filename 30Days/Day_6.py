a = int(input())

b = [input() for i in range(a)]

for string in b:
    for i in range(len(string)):
        if (i % 2 == 0):
            print(string[i], end="")
    print(" ", end="")
    for j in range(len(string)):
        if (j % 2 == 1):
            print(string[j], end="")
    print("")

