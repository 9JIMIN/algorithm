n = int(input())

num = list(range(1, n+1))


while True:
    i, j = n-1, n-1
    print(*num)
    while i>0 and num[i-1]>num[i]:
        i -= 1

    if i == 0:
        break

    while num[i-1]>num[j]:
        j -= 1

    num[i-1], num[j] = num[j], num[i-1]
    num = num[:i]+list(reversed(num[i:]))