numbers = [4, 2, 7, 4, 2, 9, 7, 7, 5]
seen = set()
duplicates = []

for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.add(num)

print(duplicates)
