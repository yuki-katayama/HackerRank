import sys


S = input().strip()
my_list = []
for s in S:
    try:
        my_list.append(int(s))
    except:
        print("Bad String")
