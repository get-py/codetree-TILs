a_arr = input().split()
a_math, a_eng = int(a_arr[0]), int(a_arr[1])
b_arr = input().split()
b_math, b_eng = int(b_arr[0]), int(b_arr[1])

if a_math > b_math and a_eng > b_eng:
    print(1)
else:
    print(2)