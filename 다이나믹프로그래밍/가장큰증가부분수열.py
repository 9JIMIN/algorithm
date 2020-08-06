# n = int(input())
# num = list(map(int, input().split()))

# a = num.copy()

# for i in range(n):
#     idx = [j for j in range(i) if num[j]<num[i]]
#     if len(idx)!=0: a[i] += max([a[i] for i in idx])
# print(max(a))

input()
num = map(int,input().split())
d = [0]*1001

for x in num:
	d[x] = max(d[:x]) + x
print(max(d))