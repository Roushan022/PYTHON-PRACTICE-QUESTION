from itertools import permutations
found=set()
for i in range(1000,10000):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        value=str(i)
        arth=[]
        for p in permutations(value):
            x=int(''.join(p))
            if x>1000:
                prime=True
                for j in range(2,int(x**0.5)+1):
                    if x%j==0:
                        prime=False
                        break
                if prime:
                    arth.append(x)
        arth=sorted(set(arth))
        for a in arth:
            for b in arth:
                if b<=a:
                    continue
                c=2*b-a
                if c in arth and c>b:
                    sequence=(a,b,c)
                    if sequence not in found:
                        print(a,b,c)
                        found.add(sequence)
        
