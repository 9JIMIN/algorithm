input()
num = map(int, input().split())
d = {}

for x in num:
    d[sum(d[i]>x for i in d)] = x
print(len(d))