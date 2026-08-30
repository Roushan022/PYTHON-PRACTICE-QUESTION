a=[]
n=int(input("Enter a the num of total elem "))
for num in range(0,n):
    nums=int(input("Enter the number "))
    a.append(nums)

remove_dub=set(a)
convert_list=list(remove_dub)
print(convert_list)
