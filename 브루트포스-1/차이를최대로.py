# n = int(input())
# num = list(map(int, input().split()))
# index = [*range(1, n+1)]
# mx = 0

# while True:
#     candidate = 0
#     for i in range(1, n):
#         candidate += abs(num[i-1] - num[i])

#     mx = max(mx, candidate)
#     i, j = n-1, n-1
#     while i>0 and index[i-1]>index[i]:
#         i -= 1
    
#     if i == 0: break

#     while index[i-1]>index[j]:
#         j -= 1
#     index[i-1], index[j] = index[j], index[i-1]
#     index = index[:i] + list(reversed(index[i:]))
#     num[i-1], num[j] = num[j], num[i-1]
#     num = num[:i] + list(reversed(num[i:]))

# print(mx)


from itertools import permutations
n = int(input())
num = list(permutations(int(i) for i in input().split()))

ans = 0
for p in num:
    candidate = sum(abs(p[i-1]-p[i]) for i in range(1, n))
    ans = max(ans, candidate)

print(ans)
