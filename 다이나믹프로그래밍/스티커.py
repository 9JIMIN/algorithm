for _ in range(int(input())):
    n = int(input())
    num = []
    for _ in range(2):
        num.append(list(map(int, input().split())))
    num[0][1] += num[1][0]
    num[1][1] += num[0][0]
    for i in range(2, n):
        num[0][i] += max(num[1][i-1], num[1][i-2])
        num[1][i] += max(num[0][i-1], num[0][i-2])
    print(max(num[0][-1], num[1][-1]))