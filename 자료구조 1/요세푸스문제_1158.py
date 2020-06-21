""" 
입력: 7 3
출력: <3, 6, 2, 7, 5, 1, 4>
"""

# 내 답안 = 시간이 오래걸림
""" import sys
input = sys.stdin.readline

nk = input().split()
n = int(nk[0])
k = int(nk[1])
stack = []
output = []

index = -1

for t in range(n):
    stack.append(t+1)

for s in range(n):
    for i in range(k):
        index += 1
        if index + 1 > len(stack):
            index = 0
    output.append(str(stack.pop(index)))
    index -= 1

output = ', '.join(output)
print(f'<{output}>') """

# 모범 답안
""" 
3 % 7 = 3 이다.
나눈 나머지값을 인덱스로 이용해서 푼 경우.. 
난 인덱스를 맞춰갈려고 했는데 그럴 필요가  
"""
N, K = map(int, input().split())
number_list = list(range(1, N+1))
answer = []
index = 0

for i in range(N):
    index += K-1
    index %= N
    answer.append( str(number_list.pop(index)) )
    N -= 1
    
print(f'<{", ".join(answer)}>')