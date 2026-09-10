a=[]
n=int(input("Enter the number of elem "))
for i in range(0,n):
    value=input(f"ENter the string {i+1}")
    a.append(value)

max_len=len(a[0])
temp=a[0]
for i in a:
    if len(i) > max_len:
        max_len=len(i)
        temp=i

print(f"the max length of the string from the list is {temp} ")
