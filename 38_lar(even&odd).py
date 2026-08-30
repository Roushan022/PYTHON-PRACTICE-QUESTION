value=int(input("Enter the number "))
b=[]
for val in range(0,value):
    a=int(input("Enter the values "))
    b.append(a)
    odd=[]
    even=[]
    b.sort()
for i in b:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even[-1])
print(odd[-1])
