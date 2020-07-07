""" 
2진수를 받아서 8진수로 변환
입력: 11001100
출력: 314
 """

n = input()

n = list(n)
ans = []
while n:
    t = 0
    for i in range(3):
        x = n.pop()
        if x == '1': t += 2**i
        if n == []: break
    ans.append(str(t))

ans = int(''.join(ans[::-1]))
print(ans)


""" 
2
- bin(), oct(), hex() 2, 8, 16 진수로 변환하는 함수
- int('101', 2) = 5 // 이진수를 10진수로 바꿔줌
- 이런걸 몰라서 저 긴 코드를 작성했구나.. 나 좀 대단한 듯?
 """
print(oct(int(input(),2))[2:])