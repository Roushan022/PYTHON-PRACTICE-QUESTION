def CommonLetter(s1,s2):
    # a=list(set(s1) & set(s2))
    s1=set(s1)
    s2=set(s2)
    a=list(s1 & s2)
    for i in a:
        print(i)
    return
n1=input("Enter a num ")
n2=input("Enter nae ")
CommonLetter(n1,n2)
