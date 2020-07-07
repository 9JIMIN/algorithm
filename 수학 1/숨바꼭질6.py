""" 
입력:
3 3
1 7 11
출력:
2

- 두번째줄 숫자 개수, 내 위치
- 동생들 위치

- 그냥 내 위치=숫자에서 둘째 줄 숫자들 뺀 값의 GCD를 구하면 된다. 
 """
# from math import gcd

# N, S = map(int, input().split())
# alist = list(map(int, input().split()))

# for i in range(N):
#     if i == 0:
#         g = alist[i] - S
#     else:
#         g = gcd(g, abs(alist[i] - S))

# print(g)

""" 
다른 답

- gcd 구하는 함수가 예술이다. 
- 내가 만든 if 문은 처음만 비교하니까, 저렇게 만들필요가 없었다.
 """

def gcd(a,b):
    return gcd(b,a%b) if b>0 else a

N,S = map(int,input().split())
L = list(map(int,input().split()))
ans = abs(S-L[0])
for i in L:
    ans = gcd(ans,abs(i-S))
print(ans)