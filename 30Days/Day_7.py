if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
for i in range(len(arr) - 1):
    print(arr[len(arr) - 1 - i], end=' ')
print(arr[0])
