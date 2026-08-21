n=int(input("Enter a number:- "))
a=[]
for i in range(n+1):
    print(i,sep=" ",end=" ")
    if (i<n):
        print("+",end=" ")
    a.append(i)
print("=",sum(a))
print()
