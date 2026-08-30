a=[]
n=int(input("Enter a the num of total elem "))
for num in range(0,n):
    nums=int(input("Enter the number "))
    a.append(nums)
value=int(input("Enter the value "))
count=0
for elem in a:
    if elem==value:
        count+=1
print(f"No of time {value} append is {count}")
