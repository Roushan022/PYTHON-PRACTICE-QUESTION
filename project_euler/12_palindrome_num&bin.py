
# print(bin(value)[2:])
total=0
i=10
while(i<1000000):
    value=i
    temp=i
    val=0
    while(temp>0):
        pal=temp%10
        val=val*10+pal
        temp//=10 

    i_bin=int(bin(i)[2:])
    value_bin=i_bin
    temp_bin=i_bin
    val_bin=0
    while(temp_bin>0):
        pal_bin=temp_bin%10
        val_bin=val_bin*10+pal_bin
        temp_bin//=10 
    if value ==val and value_bin==val_bin:
        total+=value
    i+=1
print(total)
