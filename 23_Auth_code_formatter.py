def AuthcodeFormat(value):
    count=0
    new_value=""
    for i in value:
        new_value +=i
        count+=1
        if count==3:
            new_value +=" "
            count=0
    print(new_value)
    return
AuthcodeFormat(input("Enter the data "))

