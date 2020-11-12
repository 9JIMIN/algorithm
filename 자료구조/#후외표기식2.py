n = int(input())
s, stack = input(),[]
val = [int(input()) for _ in range(n)]

for c in s:
    if "A" <= c <= "Z": stack.append(val[ord(c)-65])
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(eval(str(b)+c+str(a)))
print("%.2f"%stack[0])