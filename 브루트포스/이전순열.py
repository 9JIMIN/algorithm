n = int(input())
num = list(map(int, input().split()))

i, j = n-1, n-1

while i>0 and num[i-1]<num[i]:
    i -= 1
if i == 0:
    print(-1)
    exit()

while num[i-1]<num[j]:
    j -= 1

num[i-1], num[j] = num[j], num[i-1]
ans = num[:i]+list(reversed(num[i:]))
print(*ans)