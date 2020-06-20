import sys
input = sys.stdin.readline

nk = input().split()
n = int(nk[0])
k = int(nk[1])
stack = []
output = []

for i in range(n):
    stack.append(i+1)

for i in range(n):
    index = k * (i + 1)
    if index > len(stack) - 1:
        

output.append(stack.pop(k-1))
output.append(stack.pop(2*k-1))
output.append(stack.pop(3*k-1))
