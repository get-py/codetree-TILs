n = int(input())
sum_val = 0

for i in range(1, 100+1):
    sum_val += i
    if n <= sum_val:
        print(i)
        break