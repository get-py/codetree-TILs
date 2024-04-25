n = int(input())

for i in range(n):
    for j in range(n, 0, -1):
        if i >= j-1:
            print(n - j + 1, end=' ')
    print()