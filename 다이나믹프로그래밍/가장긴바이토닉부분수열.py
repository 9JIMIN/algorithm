# n = int(input())
# num = list(map(int, input().split()))
# left = [0] * n
# right = [0] * n
# ans = 0

# for i in range(n):
#     left[i] = 1
#     for j in range(i):
#         if num[j] < num[i] : left[i] = max(left[i], left[j] + 1)

# for i in range(n - 1, -1, -1):
#     right[i] = 1
#     for j in range(n - 1, i -1, -1):
#         if num[j] < num[i] : right[i] = max(right[i], right[j] + 1)

# for i in range(n):
#     if ans < left[i] + right[i] - 1: ans = left[i] + right[i] - 1

# print(ans)

input();
d = {}
e = {}
a = []
num = list(map(int,input().split()))
r = 0
for i in num:
    s = sum(i>d[k] for k in d)
    d[s] = i
    a[:0] = s,
for i,a in zip(num[::-1], a):
    s = sum(i > e[k] for k in e)
    e[s] = i
    r = max(r,a+s+1)
print(r)