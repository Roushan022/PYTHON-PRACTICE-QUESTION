inout_1=list(map(int,input("Enter the marks").split()))
input_sorted=sorted(inout_1,reverse=True)
output=[]
for mark in input_sorted:
    rank=1
    for other_mark in input_sorted:
        if other_mark > mark:
            rank+=1
    output.append(rank)
        
print(output)
