def PalindromCodeCheck(name):
    step_1=""
    for i in name:
        if i.isalnum():
            step_1 +=i.lower()
    og_name=step_1
    final=step_1[-1::-1]
    return og_name==final
print(PalindromCodeCheck("A Toyota"))
