# input()
# num = map(int, input().split())
# d = {}
# for n in num:
#     d[sum( n > d[k] for k in d )] = n
# print(len(d))

# n = int(input())
# num = list(map(int, input().split()))
# d = [0]*n

# for i in range(n):
#     for j in range(i):
#         if num[i] > num[j] and d[i] < d[j]:
#             d[i] = d[j]
#     d[i] += 1

# print(max(d)) 

n = int(input())
num = list(map(int, input().split()))
d = {}

for x in num:
    d[sum(x > d[i] for i in d)] = x
print(len(d))