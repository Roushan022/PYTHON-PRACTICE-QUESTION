n=int(input("Enter a the number of elements  "))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)

c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)

c.sort()
d.sort()
print(f"Highest even number {c[-1]}")
print(f"Highest old number {d[-1]}")

