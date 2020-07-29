# d = [[] for _ in range(91)]
# d[1] = ['1']
# for i in range(2, 10):
#     r = len(d[i-1])
#     for j in range(r):
#         if d[i-1][j] == '1': d[i] += ['0']
#         else: d[i] += ['0', '1']
# print(d[:10])

d = [[0, 0] for _ in range(91)]
d[1] = [0, 1]
for i in range(2, 91):
    d[i][0] = d[i-1][0]+d[i-1][1]
    d[i][1] = d[i-1][0]

n = int(input())
print(sum(d[n]))