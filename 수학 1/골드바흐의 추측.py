""" 
골드바흐의 추측 - "2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다."

- 2는 제외하고, 두 수의 차가 가장 큰 경우를 n = a + b 형태로 출력한다.
- 먼저 소수 리스트를 정의하고, 인풋을 받아서 시간을 아낀다. 
- 문제 "입력" 부분좀 잘 읽자..

입력: 8 
출력: 8 = 3 + 5


 """
import sys
input = sys.stdin.readline

def prime_list(n):
    arr = [True]*n
    m = int(n**0.5)+1
    for i in range(2, m):
        if arr[i] == True:
            for j in range(i+i, n, i):
                arr[j] = False
    return [[i for i in range(3, n) if arr[i] == True], arr]

p1 = prime_list(1000000)[0]
p2 = prime_list(1000000)[1]
n = 1
while True:
    n = int(input())
    
    if n == 0:
        break

    for i in range(n//2):
        if p2[n-p1[i]] == True:
            print(f"{n} = {p1[i]} + {n-p1[i]}")
            break

""" 
더 간결하게
 """
sieve = list(range(1000000))
sieve[1] = 0
for i in range(2,1001):
    for j in range(i*i, 1000000, i): sieve[j] = 0
prime = list(filter(lambda x:x, sieve)) # 0 제외시키기

input = __import__('sys').stdin.readline
while 1:
    n = int(input())
    if n == 0: break
    for p in prime:
        q = n-p
        if sieve[q]: print(n, '=', p, '+', q); break