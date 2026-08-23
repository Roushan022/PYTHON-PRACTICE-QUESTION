def reverse(string):
    reversed_string=""
    for char in string:
        reversed_string= char + reversed_string
    return reversed_string
name=input("Enter a string:- ")
print(reverse(name))
