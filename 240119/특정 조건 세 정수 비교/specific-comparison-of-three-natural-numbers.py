arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])


if a == int(min(arr)):
    print(1, end=' ')
else:
    print(0, end=' ')

if a == b == c:
    print(1, end=' ')
else:
    print(0, end=' ')