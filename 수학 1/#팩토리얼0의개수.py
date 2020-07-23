""" 
입력: 10
출력: 2
- 10의 팩토리얼 3628800에서 끝에 연속되는 0의 개수는 2
 """

n = int(input())

p = 1
for i in range(1, n+1):
    p *= i

c = 0
while p%10 == 0:
    c += 1
    p //= 10

print(c)
