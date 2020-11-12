from collections import Counter

n = int(input())
num = [*map(int, input().split())]

stack = []
ngf = [-1 for _ in range(n)]
c = Counter(num)

for i in range(n):
    while stack and c[num[i]] > c[num[stack[-1]]]:
        ngf[stack.pop()] = num[i]
    stack.append(i)
print(*ngf)