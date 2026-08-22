def change(string):
    new_name=string[-1]+string[1:-1]+string[0]
    return new_name
name=input("Enter a name ")
print(change(name))
