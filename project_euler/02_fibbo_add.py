limit = 4000000
a = 1
b = 2
add = 0
while a <= limit:
    if a % 2 == 0:
        add += a
    next_term = a + b
    if next_term > limit:
        break
    a, b = b, next_term
print(add)
