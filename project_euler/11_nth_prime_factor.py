# <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
# <p>What is the largest prime factor of the number $600851475143$?</p>

i = 2
count=0
while count<=10001:
    value = True

    for num in range(2, int(i ** 0.5) + 1):
        if i % num == 0:
            value = False
            break

    if value:
        count+=1
        if count==10001:
            print(i)
    i+=1
    

    
