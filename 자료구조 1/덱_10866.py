""" 
push_front X
push_back Y
pop_front
pop_back
size
empty
front
back
"""
import sys
input = sys.stdin.readline

N = int(input())
deque=[]

for i in range(N):
    com = input().strip()
    com_1 = com.split('_')[0]

    if com_1 == 'push':
        
        if com.split('_')[1].split()[0] == 'front':
            deque.insert(0, com.split()[1])
        else:
            deque.append(com.split()[1])
    elif com_1 == 'pop':
        if len(deque) == 0:
            print(-1)
        else:
            if com.split('_')[1] == 'front':
                print(deque.pop(0))
            else:
                print( deque.pop(len(deque) - 1) )
    elif com_1 == 'size':
        print(len(deque))
    elif com_1 == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif com_1 == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif com_1 == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])


