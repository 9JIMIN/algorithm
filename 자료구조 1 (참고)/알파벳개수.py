""" 
입력: jimin // 소문자만 옴.
출력: 0 0 0 0 0 0 0 0 2 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0
 """

""" 
최초답

- 따로 리스트를 만들고, 출력할 필요없이 바로바로 출력해도됨.
 """
s = input()
out = [0 for _ in range(26)]

for c in s:
    out[ord(c)-97] += 1

print(*out)


""" 
개선판

- chr() 는 ord()의 반대 ex) chr(97) -> 'a'
- 받은 단어로 루프를 도는것이 아니라, 알파벳으로 돌면서 단어 속 개수를 출력.
 """
S = input()
for i in range(26): print(S.count(chr(97 + i)), end=' ')