ID = input("Enter a number:- ")

if ID.isdigit():
    num = int(ID)
    if 999 <= num <= 1000:
        print(True)
    else:
        print(False)
else:
    print(False)
