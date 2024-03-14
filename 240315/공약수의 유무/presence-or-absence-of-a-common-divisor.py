arr = input().split()
a, b = int(arr[0]), int(arr[1])
satisfied = False
arr1 = []

for i in range(1, 1920+1):
    if 1920 % i == 0 and 2880 % i == 0:
        arr1.append(i)

for i in range(a, b+1):
    for j in arr1:
        if i == j:
            satisfied = True




if satisfied == True:
    print(1)
else:
    print(0)