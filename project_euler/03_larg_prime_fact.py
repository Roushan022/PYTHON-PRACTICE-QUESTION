n = 600851475143
ans = []
d = 2
while d * d <= n:
    while n % d == 0:
        ans.append(d)
        n //= d
    d += 1
if n > 1:
    ans.append(n)
print(ans)
    
