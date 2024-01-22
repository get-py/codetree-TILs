arr1 = input().split()
arr2 = input().split()
age1, gender1 = int(arr1[0]), arr1[1]
age2, gender2 = int(arr2[0]), arr2[1]

if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)