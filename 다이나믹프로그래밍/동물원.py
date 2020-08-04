d = [0, 3, 7]

for i in range(3, 100001):
    d.append((2*d[-1]+d[-2])%9901)

n = int(input())
print(d[n])