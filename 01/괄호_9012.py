import sys
input=sys.stdin.readline

""" 
괄호 제대로 만들었는지 확인하는거.
(())() // YES
)(())) // NO

- '(', ')' 의 수가 같아야 함.
- 중간에 ')' 의 수가 '(' 보다 커지면 안됨.

- 오래고민했는데, 규칙은 역시나 간단했다.
"""

N=int(input())

for i in range(N):
    data=input()
    
    a=0
    for d in data:
        if d=='(':
            a+=1
        elif d==')':
            a-=1

        if a<0:
            break

    if a!=0:
        print('NO')
    else:
        print('YES')