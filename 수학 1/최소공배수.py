n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    p = a * b
    while a:
        a, b = b % a, a
    print(p//b)

""" 
2

- exec를 이용하는 방법
- eval은 1+1같은 식 만 받을 수 있음, exec는 '문'을 받아서 처리가능.
 """

import math
exec('a, b = map(int, input().split()); print(a*b // math.gcd(a,b));' * int(input()))