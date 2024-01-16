inp = input()
arr = inp.split()
height = int(arr[0]) / 100
weight = int(arr[1])

bmi = weight // (height * height)

print(int(bmi))
if bmi >= 25:
    print('Obesity')