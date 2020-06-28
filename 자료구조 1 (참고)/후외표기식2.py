""" 
후위 표기식의 계산
5
ABC*+DE/-
1
2
3
4
5
출력: 6.20
 """

""" 
최초답

// 문제점
- ascii_uppercase라는 문자열 'ABCD..XYZ'를 받음(알파벳의 인덱스를 알기 위함)
- N 크키의 인덱스를 가진 리스트를 입력받아서 만드는 방법이 비효율적
- 
 """
from string import ascii_uppercase

n = int(input())
s = input()
o = []
for i in range(n):
    o.append(int(input()))
stack = []

for i in range(len(s)):
    if stack and s[i] == "+":
        q = stack.pop(-2) + stack.pop(-1)
        stack.append(q)
    elif stack and s[i] == "-":
        q = stack.pop(-2) - stack.pop(-1)
        stack.append(q)
    elif stack and s[i] == '*':
        q = stack.pop(-2) * stack.pop(-1)
        stack.append(q)
    elif stack and s[i] == "/":
        q = stack.pop(-2) / stack.pop(-1)
        stack.append(q)
    else:
        stack.append(o[ascii_uppercase.index(s[i])])

print("%0.2f" % stack[0])

""" 
개선판

- o 리스트를 간단하게 만들기
- ord()는 아스키코드를 리턴 ex) ord('A') -> 65, ord('B') -> 66
- eval()은 string을 실행시키는 함수다. ex) eval('5+5') -> 10 
 """

n = int(input())
s, stack = input(),[]
val = [int(input()) for _ in range(n)]

for c in s:
    if "A" <= c <= "Z": stack.append(val[ord(c)-65])
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(eval(str(b)+c+str(a)))
print("%.2f"%stack[0])