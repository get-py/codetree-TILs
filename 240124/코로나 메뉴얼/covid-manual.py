arr1 = input().split()
arr2 = input().split()
arr3 = input().split()

sym1, tem1 = arr1[0], int(arr1[1])
sym2, tem2 = arr2[0], int(arr2[1])
sym3, tem3 = arr3[0], int(arr3[1])

if (sym1 == 'Y' and tem1 >= 37) and (sym2 == 'Y' and tem2 >= 37):
    print('E')
elif (sym1 == 'Y' and tem1 >= 37) and (sym3 == 'Y' and tem3 >= 37): 
    print('E')
elif (sym2 == 'Y' and tem2 >= 37) and (sym3 == 'Y' and tem3 >= 37):
    print('E')
else:
    print('N')