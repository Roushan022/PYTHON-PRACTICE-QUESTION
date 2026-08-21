import math as m
a=int(input("Enter 1st number:- "))
b=int(input("Enter 2nd number:- "))
print("GCD of the numebr of ",m.gcd(a,b))


Recusrion Method
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter  a num:- "))
b=int(input("Enter another number:- "))
GCD=gcd(a,b)
print(GCD)
