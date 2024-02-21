n = int(input())
sum_val = 0

for i in range(n):
    a = int(input())
    sum_val += a

avg = sum_val / n

print(sum_val, f"{avg:.1f}")