total=0
for i in range(1,1001):
  total+=i**i
last_ten=str(total)
print(type(last_ten))
print(last_ten[-10:])
