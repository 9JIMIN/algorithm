n = int(input())
price = list(map(int, input().split()))

ans = [0]
for i in range(1,n+1):
    ans.append(max(ans[i-j-1] + price[j] for j in range(i)))
print(ans[-1])