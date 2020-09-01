from itertools import combinations
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

combi = list(combinations(range(n), n//2))
length = len(combi)
team_a = []
for c in combi[:length//2]:
    x = 0
    for k in combinations(c, 2):
        x += s[k[0]][k[1]]+s[k[1]][k[0]]
    team_a.append(x)

team_b = []
for c in reversed(combi[length//2:]):
    x = 0
    for k in combinations(c, 2):
        x += s[k[0]][k[1]]+s[k[1]][k[0]]
    team_b.append(x)

ans = 100
for i in range(length//2):
    ans = min(ans, abs(team_a[i]-team_b[i]))

print(ans)