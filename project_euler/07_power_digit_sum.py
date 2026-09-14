def Power_Sum(n,m):
    total=0
    power=n**m
    power_dig=str(power)
    for i in range(len(power_dig)):
        total+=int(power_dig[i])
    return total

print(Power_Sum(2,1000))
