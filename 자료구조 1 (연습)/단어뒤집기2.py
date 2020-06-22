""" 
태그안 내용을 공백으로 변경
띄어쓰기 나눠서 뒤집음
태그안 내용을 다시 채워넣음

모르겠다. 내일 다시 생각해보자,.
"""
import sys
import re
input = sys.stdin.readline

line = input()

regex = re.compile(r"\<([A-Za-z0-9 ]+)\>")

tags = re.findall(regex, line)
line = re.sub(regex, "#", line)
print(line)
answer = []
for i in line.split():
    answer.append(i[::-1])

answer = " ".join(answer)
print(answer)

for t in range(len(tags)):
    answer = answer.replace('#', f"<{tags[t]}>", 1) # 끝에 1 넣으면 한번만 바꿈.

print(answer)
