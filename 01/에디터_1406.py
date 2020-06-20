""" 
계속 시간초과가 떠서, 
다른 분의 답을 참고 했다.

시간복잡도 관련해서 공부를 좀 해야할 듯. 
그리고 c++을 배워야겠다는 생각이 드네.
"""
""" 
커서 위치에 따라 좌, 우 2개의 리스트로 나누는 방법
list()로 리스트 만들고, ''.join()으로 합치기
"""

import sys
line = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

stack_1 = list(line)
stack_2 = []

for s in range(N):
    x = sys.stdin.readline().rstrip()

    if x == "L" and stack_1:
        stack_2.append(stack_1.pop())
    elif x == "D" and stack_2:
        stack_1.append(stack_2.pop())
    elif x == "B" and stack_1:
        stack_1.pop()
    else:
        if x[0] == "P":
            stack_1.append(x[2])

print(''.join(stack_1 + stack_2[::-1]))



# 이거는 내가 쓴 코드, 시간초과 뜸.
""" import sys
input=sys.stdin.readline

# 'L' : 커서를 왼쪽으로 한 칸, 맨 앞이면 무시
# 'D' : 커서를 오른쪽으로 한 칸, 맨 뒤면 무시
# 'B' : 커서 왼쪽의 문자를 삭제, 맨 앞이면 무시
# 'P $' : $를 커서 왼쪽에 추가함.


# 데이타 받기
line = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

stage=[]
for n in range(N):
    stage.append(input().strip())


# 데이타 처리
cursor = len(line)

for s in stage:
    if s == 'L':
        if cursor > 0:
            cursor -= 1
        else:
            cursor = 0
    elif s == 'D':
        if cursor < len(line):
            cursor += 1
        else:
            cursor = len(line)
    elif s == 'B':
        if cursor > 0:
            line = line[:cursor-1] + line[cursor:]
            cursor -= 1
        else:
            cursor = 0
    elif s.split()[0]=='P':
        line = line[:cursor] + s.split()[1] + line[cursor:]
        cursor += 1


# 데이타 출력
print(line) """