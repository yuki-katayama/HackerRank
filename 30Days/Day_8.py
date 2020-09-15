my_dict = {}
my_list = []

num = int(input())

for i in range(num):
    key, value = input().split()
    my_dict[key] = value

while True:
    try:
        string = input()
        if(string in my_dict):
            print(string, "=", my_dict[string], sep="")
        else:
            print("Not found")
    except:
        break
