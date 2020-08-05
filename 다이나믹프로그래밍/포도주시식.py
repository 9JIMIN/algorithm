# n = int(input())
# num = [int(input()) for _ in range(n)]
# d = [0]
# d.append(num[0])
# if n > 1: d.append(num[0]+num[1])

# for i in range(3, n+1):
#     a = num[i-1] + d[i-2]
#     b = num[i-1] + num[i-2] + d[i-3]
#     c = d[i-1]
#     d.append(max(a,b,c))
# print(d[n])

d = (0,)*3
for _ in range(int(input())):
    p = int(input())
    d = d[1]+p, d[2]+p, max(d)
    print(d)
print(max(d))