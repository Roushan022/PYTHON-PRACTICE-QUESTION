def Extvalidator(files):
    types=files[(len(files)-4):len(files)].lower()
    print(types)
    if types==".jpg" or types== ".png" or types==".pdf":
        print(True)
    else:
        print(False)
    return
files=input("Enter the name with tyoe of  your file:- ")
Extvalidator(files)
