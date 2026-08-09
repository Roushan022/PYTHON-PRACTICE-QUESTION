def TitleSlugGen(name):
    nameLower=name.lower()
    url=""
    for i in nameLower:
        if i.isalnum():
            url +=i
        elif i==" ":
            url+="-"
    print(url)
    return
DomainName=input("Enter name of the e-commerce:- ")
TitleSlugGen(DomainName)
