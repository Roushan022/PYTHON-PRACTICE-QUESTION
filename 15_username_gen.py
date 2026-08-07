def Username_gen(name):
    first,last=name.split(" ")
    user_name=(first[0]+last).lower()
    print(user_name)
name=input("Enter your full name")
Username_gen(name)
