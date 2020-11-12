""" 
입력: Baekjoon Online Judge123
출력: Onrxwbba Bayvar Whqtr123

- 알파벳만 13개씩 미룸.
- 알파벳은 총 26개. 그래서 암호화를 두 번하면 원래대로.

 """

S = list(input())

for i in range(len(S)):
    index = ord(S[i])
    if 65 <= index <= 90:
        if index + 13 > 90: 
            S[i] = chr(ord(S[i]) - 13)
        else: 
            S[i] = chr(ord(S[i]) + 13)
    elif 97 <= index <= 122:
        if index + 13 > 122:
            S[i] = chr(ord(S[i]) - 13)
        else:
            S[i] = chr(ord(S[i]) + 13)

print("".join(S))

""" 
- codecs 모듈을 이용하는 방법
 """
import codecs
print(codecs.getencoder('rot-13')(input())[0])