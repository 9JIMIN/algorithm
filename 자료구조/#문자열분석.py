# import sys
# while 1:
#     ans = [0, 0, 0, 0]
#     s = sys.stdin.readline()
#     if not s: break

#     for n in s:
#         if n.islower(): ans[0] += 1
#         if n.isupper(): ans[1] += 1
#         if n.isnumeric(): ans[2] += 1
#         if n.isspace(): ans[3] += 1
#     print(*ans)

import sys

while True:
    out = [0, 0, 0, 0]
    n = sys.stdin.readline()
    if not n: break
    for i in n:
        if i.islower():
            out[0] += 1
        elif i.isupper():
            out[1] += 1
        elif i.isnumeric():
            out[2] += 1
        elif i == " ":
            out[3] += 1
    print(*out)