int_val=int(input("Enter the number "))
fact=1
for i in range(1,int_val+1):
    fact*=i
print(fact)
new=0
for val in str(fact):
    sum+=int(val)
print(type(int_val))
print(sum)
