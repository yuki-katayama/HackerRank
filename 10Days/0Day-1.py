from decimal import Decimal, ROUND_HALF_UP

a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
sum_under = 0
sum_over = 0

for i in range(a):
    sum_under += c[i]
    sum_over += b[i] * c[i]

print(Decimal(sum_over/sum_under).quantize(Decimal('0.1'), ROUND_HALF_UP))
