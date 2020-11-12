a, b = map(int, input().split())
p = a * b
while a:
    a, b = b%a, a

print(b)
print(p//b)