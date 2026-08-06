import math
def magnitude(x,y):
    print(math.sqrt(x**2+y**2))
    z=complex(x,y)
    print(z)
    print(abs(z))
print("Z=R+Xj")
R=int(input("Enter the value of R:- "))
X=-int(input("Enter the value of X:- "))
magnitude(R,X)

