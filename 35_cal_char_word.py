def count(sentence):
    charr=0
    word=1
    for char in sentence:
        if char !=" ":
            charr +=1
        else:
            word +=1
    print("Char count :- ",charr)
    print("Word count :- ",word)
    return

sent=input("Enter a sentence ")
count(sent)
