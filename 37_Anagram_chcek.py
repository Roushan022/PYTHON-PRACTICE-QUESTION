s1=input("Enter first string ")
s2=input("Enter second string ")
s_1=s1.lower()
s_2=s2.lower()
#anagram 
if (sorted(s_1))==sorted(s_2):
    print("The Strings are anagrams. ")
else:
    print("The strings aren't anagrams. ")
