num = int(input())
my_list = list(int(input()) for _ in range(num))

for index, i in enumerate(my_list):
    judge = 0
    if(i == 1):
        print("Not prime")
    elif(i == 2):
        print("Prime")
    elif(i % 2 == 1):
        for k in range(3, i, 2):
            if(i % k == 0):
                judge = 1
                print("Not prime")
                break
            if(k ** 2 > i):
                break
        if(judge == 0):
            print("Prime")
    else:
        print("Not prime")
