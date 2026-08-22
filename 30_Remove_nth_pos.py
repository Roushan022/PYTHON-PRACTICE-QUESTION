def remove(string,n):
    new_name=string[0:n]+string[n+1:]
    return new_name
Name=input("Enter a name")
nth=int(input("Enter the pos number "))
nth=nth-1
print(remove(Name,nth))
