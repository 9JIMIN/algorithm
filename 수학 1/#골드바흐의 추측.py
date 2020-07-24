*s, = range(1000001)
for i in range(2, 1001):
    if s[i]:
        s[2*i::i] = [0]*(1000000//i-1)
prime = [x for x in s if x>1] # 0은 False라서 제외된다.

input = __import__('sys').stdin.readline
while 1:
    n = int(input())
    if n == 0: break
    for p in prime:
        q = n-p
        # if q in prime: print(n, '=', p, '+', q); break 시간초과남.
        if s[q]: print(n, '=', p, '+', q); break