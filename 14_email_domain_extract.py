# split when @ arrive 
email=map(input("Enter the email:- ").split())
new_part=email.split("@")
domain=[e.split("@")[1] for e in email] # updated version 
print(new_part[1])
print(domain)
print(new_part[1])
