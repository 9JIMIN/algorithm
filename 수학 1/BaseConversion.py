""" 
입력:
17 8 // A진법, B진법
2 // 주어지는 수의 자릿수의 개수
2 16 // 이게 하나의 숫자임. 자릿수는 2자리 => 10진법으로 2*17+16=50
출력:
6 2
 """

A, B = map(int, input().split())
L = int(input())
N = list(map(int, input().split()))

ten = 0
for i in range(L):
    ten += N[-(i+1)]*(A**i)

eight = []
while ten:
    eight.append(ten % B)
    ten //= B

for i in range(len(eight)):
    print(eight.pop(), end=" ")