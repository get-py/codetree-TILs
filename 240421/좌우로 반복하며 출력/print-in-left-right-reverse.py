n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(n):
            print(n - j, end='')
    else:
        for j in range(1, n+1):
            print(j, end='')
    print()