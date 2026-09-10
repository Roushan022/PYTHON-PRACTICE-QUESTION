import random as ran
a=[]
n=int(input("Enter the number of random elem want to gen:-"))
for i in range(0,n):
    a.append(ran.randint(1,20))
print(f"Random number list is : {a}")
