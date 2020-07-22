s = input()
stack = []
answer = []
pr = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2}

for c in s:
    if c in '+-*/':
        while stack and pr[c] <= pr[stack[-1]]:
            answer.append(stack.pop())
        stack.append(c)
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    else:
        answer.append(c)
while stack: answer.append(stack.pop())
print(''.join(answer))