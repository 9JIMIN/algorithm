n = list(map(int, input().split()))

sol1 = (n[0] + n[1]) % n[2]
sol2 = ((n[0] % n[2]) + (n[1] % n[2])) % n[2]
sol3 = (n[0] * n[1]) % n[2]
sol4 = ((n[0] % n[2]) * (n[1] % n[2])) % n[2]

print(sol1)
print(sol2)
print(sol3)
print(sol4)