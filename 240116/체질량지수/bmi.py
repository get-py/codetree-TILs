inp = input()
arr = inp.split()
height = int(arr[0]) 
weight = int(arr[1])
bmi = weight * 100 * 100 // (height * height)

print(bmi)
if bmi >= 25:
    print('Obesity')