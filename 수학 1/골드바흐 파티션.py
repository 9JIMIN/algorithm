""" 
- 짝수는 두 소수의 합이다. 합의 조합이 몇 개가 가능한지를 출력!
입력: 
5 // 입력개수
6
8
10
12
100

출력:
1 // 3,3
1 // 3,5
2 // 3,7|5,5
1 // 5,7
6

 """
input = __import__('sys').stdin.readline
n = int(input())

sieve = list(range(1000000))
for i in range(2, 1001):
    for j in range(i*i, 1000000, i):
        sieve[j] = 0
prime = list(filter(lambda x: x, sieve))[1:]

for i in range(n):
    m = int(input())

    par = 0
    j = 0
    while prime[j] < m//2+1:
        q = m - prime[j]
        if sieve[q]: par += 1
        j += 1
    print(par) 

""" 
덱으로 푸는 방법
- 시간 단축 됨.
- 내 답에서 prime리스트를 만드는 과정은 불필요한듯.
 """
from collections import deque
primes = deque()
chck=[False]*1000001
for i in range(2, 1000001):
    if chck[i]==False:
        primes.append(i)
        for j in range(2*i,1000001,i):
            chck[j]=True


for tc in range(int(input())):
    n = int(input())
    ans=0
    for p in primes:
        if n-p>=2 and p<=n-p:
            if chck[n-p]==False:
                ans+=1
        else:break
    print(ans)