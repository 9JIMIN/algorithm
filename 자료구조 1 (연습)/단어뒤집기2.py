""" 
처음에는 <>안 내용을 옮기고, 
남은 내용을 띄워쓰기로 나눠서 뒤집는 방식을 시도했다. 
하지만, 비효율적이었다. 

그래서 문자열의 인덱스를 살피며 괄호내용이 있으면 해당 내용을 answer리스트에 append, 
그리고 괄호 밖 문자에 대해서는 문자가 끝날때까지(인덱스 초과, 띄워쓰기, 괄호시작)
reverse리스트에 추가후, 그걸 뒤집어서 answer에 append하였다. 

단어 뒤집기1 에서는 전체를 띄워쓰기로 split을 하였지만,
이번 문제처럼 예외가 있는 경우에는 문자열을 인덱스로 읽어가는 방식으로 해야한다.
"""
line = input()
answer = []
reverse = []

i = 0

while i < len(line):
    if line[i] == '<':
        while line[i] != '>':
            answer.append(line[i])
            i += 1
        answer.append('>')
        i += 1
    else:
        while i < len(line) and line[i] != ' ' and line[i] != '<':
            reverse.append(line[i])
            i += 1
        reverse = ''.join(reverse)
        answer.append(reverse[::-1])
        reverse = []

        if i == len(line):
            break
        if line[i] == ' ':
            answer.append(' ')
            i += 1

print(''.join(answer))

""" 
다른분의 방법. 
내가 처음에 실패했던, regex를 이용함.

괄호내용을 기준으로 split하는 방법.
re.split부터 print의 end지정, map, lambda까지 배울 것이 많은 답이다.
"""
# import re
# line = input()
# match = re.split(r"(\<.*?\>)", line)
# for e in match:
#     if not e or e[0] == '<':
#         print(e, end="")
#     else:
#         print(" ".join(map(lambda x: x[::-1], e.split())), end="")