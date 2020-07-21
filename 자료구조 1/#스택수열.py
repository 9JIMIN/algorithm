import sys
input = sys.stdin.readline

data = [int(input()) for _ in range(int(input()))]

stack, answer, i = [0], [], 0
p = True

for _ in range(len(data)):
    if data[0] >= stack[-1]:
        while data[0] != stack[-1]:
            i += 1
            stack.append(i)
            answer.append('+')
        stack.pop()
        answer.append('-')
        data.pop(0)
    else:
        print('NO')
        exit()

print('\n'.join(answer))