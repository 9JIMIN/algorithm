input()
num = map(int, input().split())
d = {}
for n in num:
    d[sum( n > d[k] for k in d )] = n
print(len(d))