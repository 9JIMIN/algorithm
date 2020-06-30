import math 

def isPrime(num): 
    if num == 1: return False

    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False 
    return True

m, n = map(int, input().split()) 
for k in range(m, n+1): 
    if isPrime(k): print(k)

""" 
2
 """

m, n = map(int, input().split())
s = [*range(n + 1)]
for i in s[2:]:
    if s[i]:
        s[2*i: :i] = [0] * (n // i - 1)
        if i >= m:
            print(i)