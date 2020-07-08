""" 
입력: 60466175 36 // 10진법의 수를 받고, 다른 진법으로 바꿔서 출력
출력: ZZZZZ
 """
N, B = map(int, input().split())
ans = []

while N:
    x = N % B
    if x > 9: x = chr(x+55)
    else: x = str(x)
    ans.append(x)
    N //= B

print(''.join(ans[::-1]))