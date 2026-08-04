weight=float(input("Enter weight(kg): - "))
height=float(input("Enter height(m):- "))
bmi=round(weight/(height**2),2)  # BMI calculator formula and round of two
if bmi<18.5:
    print(f"BMI is {bmi} , you are Underweight ")
elif bmi >=18.5 or bmi<=24.9:
    print(f"BMI is {bmi}, You are in Normal zone ")
else:
    print(f"BMI is {bmi} , you are overweight ")
    
