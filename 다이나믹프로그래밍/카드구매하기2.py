n = int(input())
price = list(map(int, input().split()))

d = [0]
for i in range(1, n+1):
    d.append(min(d[i-j-1]+price[j] for j in range(i)))

print(d[-1])