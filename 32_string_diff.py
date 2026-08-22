s1=input("Enter the first String ")
s2=input("Enter the 2nd String ")
value=list(set(s1)-set(s2))
for val in value:
    print(val, end=" ")
