import re

line = input()
match = re.split(r"(\<.*?\>)", line)
for a in match:
    if not a or a[0]=='<':
        print(a, end='')
    else:
        print(' '.join(s[::-1] for s in a.split()), end='')