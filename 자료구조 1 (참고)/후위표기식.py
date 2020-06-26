""" 
입력: ((A+B)*(C+D)*(E+F))+H/G
출력: AB+CD+*EF+*HG/+
 """

""" 
- 1
 """
s = input()
stack = []
pr = {"(":0, ")":0, "+":1, "-":1, "*":2, "/":2}
out = []
for c in s:
    if c in "+-*/":
        while stack and pr[c] <= pr[stack[-1]]: out.append(stack.pop())
        stack.append(c)
    elif c == "(": stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(": out.append(stack.pop())
        stack.pop()
    else: out.append(c)
while stack: out.append(stack.pop())

print(''.join(out))


""" 
- 2
 """
# s = [" "]
# ans = []

# for c in input():
#     if c == ')':
#         while s[-1] != '(':
#             ans += s.pop()
#         s.pop()
#     elif c in "+-*/(":
#         while c != '(' and (s[-1] in "*/" or s[-1] in "-+" and c in "-+"):
#             ans += s.pop()
#         s.append(c)
#     else:
#         ans += c

# ans += reversed(s)
# print("".join(ans).strip())

""" 
- 3
 """
# def priority(x) :
 
#     if x == "*" or x == "/" :
#         return 2
#     elif x == "+" or x == "-" :
#         return 1
#     elif x == "(" or x == ")" :
#         return 0
 
#     return -1
 
# def solve() :
 
#     X = input()
 
#     ans = ""
#     stack = []

#     for c in X :

#         p = priority(c)
        
#         if c == '+' or c == '-' or c == '*' or c == '/':
#             while stack and priority(stack[-1]) >= p :
#                 ans += stack.pop()
#             stack.append(c)
#             continue
#         elif c == '(' :
#             stack.append(c)
#             continue
#         elif c == ')' :
#             while stack and stack[-1] != "(" :
#                 ans += stack.pop()
#             stack.pop()
#             continue
 
#         ans += c
 
#     while stack :
#         ans += stack.pop()
#     print(ans)
 
# solve()
