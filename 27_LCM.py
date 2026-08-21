a=int(input("Enter the first no:- "))
b=int(input("Enter the first no :- "))
if (a>b):
    min1=a              # a number which is divisible by both number
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0:
        print("LCM:- ",min1)
        break;
    min1+=1
