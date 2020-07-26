# 탑다운 방식
# N = int(input())
# def f(n):
#     if n == 1: return 1
#     elif n == 2: return 2
#     elif n == 3: return 4
#     else: return f(n-1)+f(n-2)+f(n-3)

# for _ in range(N): print(f(int(input())))


# 바텀업 방식
N = int(input())
for _ in range(N):
    a, b, c = 0, 0, 1
    for _ in range(int(input())): a, b, c = b, c, a+b+c
    print(c)
