""" 
입력: ZZZZZ 36 // 36진법의 수가 주어진다. 10이상은 알파벳으로 대체함 (A=10, B=11...)
출력: 60466175 // 10진법으로 변환해서 출력
 """

N, B = input().split()
B = int(B)
ans = 0

def toten(x, B, i):
    return x*(B**i)

for i in range(len(N)):
    n = N[-(i+1)] 
    if n in [*map(str, list(range(10)))]:
        ans += toten(int(n), B, i)
    else:
        ans += toten(ord(n)-55, B, i) # ord('A') = 65

print(ans)