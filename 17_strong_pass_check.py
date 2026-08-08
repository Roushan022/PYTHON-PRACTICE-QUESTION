def strongpass(pw):
    has_upper=any(c.isupper() for c in pw)
    has_digit=any(c.isdigit() for c in pw)
    has_special=any(c in "#!$%" for c in pw)
    return len(pw)>=8 and has_digit and has_special and has_upper
Pass=input("Enter a strong pass:- ")
print(strongpass(Pass))
