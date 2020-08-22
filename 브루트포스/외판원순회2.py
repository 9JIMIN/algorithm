from itertools import permutations

n = int(input())
price = [list(map(int, input().split())) for _ in range(n)]
per = permutations(range(1, n), n-1)
ans = 10**9

for p in per:
  index = (0,) + p + (0,) # 양끝에 0을 붙임.
  total, flag = 0, 1
  for i in range(1, n+1):
    if price[index[i-1]][index[i]] == 0:
      flag = 0; break
    total += price[index[i-1]][index[i]]
  if flag: 
      ans = min(ans, total)
print(ans)