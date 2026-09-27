i = 144
while True:
    h = i * ((2*i) - 1)
    for j in range(2, i * 2):
        p = j * ((3*j) - 1) // 2
        if p == h:
            print(h, p)
            break
    if p == h:
        break
    i += 1
