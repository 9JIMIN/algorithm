M, N = map(int,input().split())
*s, = range(N+1)
r = int(N**0.5 + 1)
for i in range(2, r):
    if s[i]:
        s[2*i::i]=[0]*(N//i-1)
sieve = filter(lambda x: (x>1 and x>=M), s)
for a in sieve: print(a)