price=int(input("Enter the total bill "))
per=int(input("How much tip you want to give (percentage)"))
people=int(input("How many people t split the bill "))
total=(price*per)//100
total_pay=price+total
pay=total_pay//people
print((pay,2))
