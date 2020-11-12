#부호와 합이 일치하는지 확인하는 함수
def ck(idx):
    hap = 0
    for i in range(idx, -1, -1):
        hap += ans[i]
        if hap == 0 and s[i][idx] != 0:
            return False
        elif hap < 0 and s[i][idx] >= 0:
            return False
        elif hap > 0 and s[i][idx] <= 0:
            return False
    return True

def solve(idx):
    if idx == n:
        return True
    if s[idx][idx] == 0:
        ans[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        ans[idx] = s[idx][idx] * i
        if ck(idx) and solve(idx+1):
            return True
    return False

n = int(input())
signs = list(input())
s = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        temp = signs.pop(0)
        if temp == '+':
            s[i][j] = 1
        elif temp == '-':
            s[i][j] = -1

ans = [0] * n
solve(0)
print(' '.join(map(str, ans)))