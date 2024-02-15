n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

for i in numbers:    
    if i % 2 == 1 and i % 3 == 0:
        print(i)