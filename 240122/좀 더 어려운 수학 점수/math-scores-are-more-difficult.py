a_arr = input().split()
a_math = int(a_arr[0])
a_eng = int(a_arr[1])

b_arr = input().split()
b_math = int(b_arr[0])
b_eng = int(b_arr[1])

if a_math == b_math:
    if a_eng > b_eng:
        print('A')
    else:
        print('B')
elif a_math > b_math:
    print('A')
else:
    print('B')