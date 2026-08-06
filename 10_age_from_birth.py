from datetime import datetime
current_year=datetime.now().year
birth_year=int(input("Enter your dob year "))
age=current_year-birth_year
if age < 13:
    print(f"Child {age}")
elif 13<=age<19:
    print(f"teen {age}")
else:
    print(f"Adult {age}")
