import sys
input = sys.stdin.readline
n = int(input())
s = set()

for _ in range(n):
    com = input().split()

    if com[0] == 'add':
        s.add(com[1])
    elif com[0] == 'remove' and com[1] in s:
        s.remove(com[1])
    elif com[0] == 'check':
        print(1 if com[1] in s else 0)
    elif com[0] == 'toggle':
        if com[1] in s: s.remove(com[1])
        else: s.add(com[1])
    elif com[0] == 'all':
        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    elif com[0] == 'empty':
        s = set()
    print(s)