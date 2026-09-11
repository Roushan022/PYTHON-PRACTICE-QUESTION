largest = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        value = i * j
        if value > largest and str(value) == str(value)[::-1]:
            largest = value

print(largest)
