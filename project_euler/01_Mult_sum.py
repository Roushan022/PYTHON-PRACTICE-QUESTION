sum=0
for _ in range(1000):
    if _ % 3 ==0 or _ % 5==0:
        sum+=_
print(sum)

summ = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(summ)
