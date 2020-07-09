""" 
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

3가지의 연산이 가능하다. 
- 1로 만드는 최솟값을 구하라.

입력: 10 // 10-1=9/3=3/3=1 -- 3번의 연산
출력: 3

다이나믹 프로그래밍이란, 문제를 작게 나눠서 푸는 방법

이런 문제는 처음이라 접근을 아예 잘 못했다. 이제 알았으니, 다음부턴 잘 하자.
 """

N = int(input())

result = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        result[i] = 0
        continue
    result[i] = result[i-1] + 1
    if i % 3 == 0 and result[i//3] + 1 < result[i]:
        result[i] = result[i//3] + 1
    if i % 2 == 0 and result[i//2] + 1< result[i]:
        result[i] = result[i//2] + 1
        
print(result[N])

""" 
2
 """
def f(n):
    if n <= 2: return n-1
    return 1 + min(f(n//3)+n%3, f(n//2)+n%2)

print(f(int(input())))

""" 
3
 """
f=lambda n:n-1 if n<3 else 1+min(f(n//2)+n%2,f(n//3)+n%3)
print(f(int(input())))