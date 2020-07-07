""" 
- 가능한 모든 쌍의 GCD의 합, 처음 몇개 할건지 나오고, 
- 다음줄부터 첫번째 숫자는 이어질 숫자들 개수
- 입력:
3
4 10 20 30 40
3 7 5 12
3 125 15 25
- 출력: 
70
3
35 

- gcd구하는 함수
- combinations 만들어서 더해주기만 하면 됨
 """
from itertools import combinations

def gcd(a, b):
    while a:
        a, b = b%a, a
    return b

n = int(input())

for i in range(n):
    num = list(map(int, input().split()[1:]))
    c = list(combinations(num, 2))
    ans = 0
    for j in c:
        p = gcd(j[0], j[1])
        ans += p

    print(ans)
    