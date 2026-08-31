input_1 = [10, 5, 20, 8, 20, 15]

largest = float('-inf')
second = float('-inf')

for num in input_1:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest")
else:
    print(second)
