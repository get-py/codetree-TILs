cnt = 0
sum_ages = 0

while True:
    n = int(input())
    if n >= 20 and n < 30:
        cnt += 1
        sum_ages += n
        continue
    else:
        avg = sum_ages / cnt
        print(f'{avg:.2f}')
        break