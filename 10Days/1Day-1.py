# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

nasi = int(input())

a = list(map(int, input().split()))

std = statistics.pstdev(a)
print(round(std, 1))