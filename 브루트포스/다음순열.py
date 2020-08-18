N = int(input())
A = list(map(int, input().split()))

i = N-1
while i>0 and A[i-1]>A[i]:
    i -= 1

if i == 0:
    print(-1)
    exit()

j = N-1
while A[i-1]>A[j]:
    j -= 1

A[i-1], A[j] = A[j], A[i-1]
print(*(A[:i]+list(reversed(A[i:]))))