import sys
input = sys.stdin.readline

"""
리스트 push 2 이런식으로 정수를 추가함. 
그리고, 아래 함수에 대한 결과를 출력 
push, top, pop, empty, size

- pop(빼낼 인덱스번호)
- insert(넣을 인덱스번호, 넣을 값)
"""

N=int(input())
stack=[]

for i in range(N):

  data=input().split()
  
  if data[0]=='push':
    stack.insert(0,int(data[1]))

  elif data[0]=='top':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[0])

  elif data[0]=='pop':
    if len(stack)==0:
      print(-1)
    else:
      d=stack.pop(0)
      print(d)

  elif data[0]=='size':
    print(len(stack))

  elif data[0]=='empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)