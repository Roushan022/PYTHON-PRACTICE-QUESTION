total=0
list=[]
for i in range(101):
    list.append(i*i)
    total=total+i
sums=sum(list)
square_sum=total**2
diff=square_sum-sums
print(diff)
