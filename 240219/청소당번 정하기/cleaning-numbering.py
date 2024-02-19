n = int(input())

cnt_class = 0
cnt_floor = 0
cnt_rest = 0

for i in range(1, n+1):
    if i % 12 == 0:
        cnt_rest += 1
    elif i % 3 == 0:
        cnt_floor += 1
    elif i % 2 == 0:
        cnt_class += 1

print(cnt_class, cnt_floor, cnt_rest)