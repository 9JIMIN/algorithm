import sys
input = sys.stdin.readline

N = int(input())

stack=[]

for i in range(N):
    x = input().rstrip()
    a = x[1]

    if a == 'u': # push
        stack.append(x.split()[1])
    elif a == 'o': # pop
        if len(stack) > 0:
            print(stack.pop(0))
        else:
            print(-1)
    elif a == 'i': # size
        print(len(stack))
    elif a == 'm': # empty
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a == 'r': # front
        if len(stack) > 0:
            print(stack[0])
        else:
            print(-1)
    elif a == 'a': # back
        if len(stack) > 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)
        

        
