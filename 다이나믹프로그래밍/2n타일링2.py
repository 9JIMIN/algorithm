a,b=1,3
for _ in range(int(input())-1):
    a, b = b, 2*a+b
print(a%10007)
