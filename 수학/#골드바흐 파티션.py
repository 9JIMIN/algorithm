*s, = range(1000001)
for i in range(2, 1001):
    if s[i]:
        s[2*i::i] = [0]*(1000000//i-1)
prime = [x for x in s if x>1]

for _ in range(int(input())):
    n = int(input())
    ans=0
    for p in prime:
        if s[n-p] and p<=n-p: ans+=1
    print(ans)