while True:
    arr = input().split()
    x, y, cha = arr[0], arr[1], arr[2]
    print(int(x)*int(y))

    if arr[2] == 'C':
        break