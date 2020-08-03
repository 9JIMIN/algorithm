# n = int(input())

# p = list(map(int, input().split()))
# index = [0, 1, 2]
# for _ in range(n-1):
#     num = list(map(int, input().split()))
#     for i in range(3):
#         m = 1001
#             c = 0
#         for j in range(3):
#             if j != index[i] and m > num[j]:
#                 m = num[j]
#                 c = j
#         index[i] = c
#         p[i] += num[c]
# print(min(p))

n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, n):
    p[i][0] += min(p[i-1][1], p[i-1][2]) 
    p[i][1] += min(p[i-1][0], p[i-1][2]) 
    p[i][2] += min(p[i-1][0], p[i-1][1])

print(min(p[-1][0], p[-1][1], p[-1][2])) 