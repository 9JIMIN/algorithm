""" 
(( 가 나오면 stick += 1
()가 나오면 answer += a
)) 가 나오면 stick -= 1 그리고 answer += 1
"""
line = input()

answer = 0
stick = 0

for i in range(len(line) - 1):
    if line[i] == '(' and line[i+1] == '(':
        stick += 1
    elif line[i] == '(' and line[i+1] == ')':
        answer += stick
    elif line[i] == ')' and line[i+1] == ')':
        stick -= 1
        answer += 1
print(answer)