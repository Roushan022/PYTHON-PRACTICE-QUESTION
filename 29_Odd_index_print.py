string=input("Enter a string ")
final=""
for i in range(len(string)):
    if i%2!=0:
        final=final+string[i]
print(final)


def modify(value):
    final=""
    final=value[1:len(value):2]
    return final
name=input("Enter a string")
print(modify(name))
