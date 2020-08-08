# n = int(input())
# num = list(map(int, input().split()))
 
# left, right = [0]*n, [0]*n
# left[0], right[-1] = num[0], num[-1]
# for i in range(1,n):
#     left[i] = max(left[i-1] + num[i], num[i])
#     right[-(i+1)] = max(right[-i]+num[-(i+1)], num[-(i+1)])
   
# mid = [0]*n
# for i in range(n):
#     if i == 0 or i == n-1:
#         mid[i] = num[i]
#     else:
#         mid[i] = left[i-1] + right[i+1]
 
# ans = max(max(left), max(mid))
# print(ans)

n = int(input())
num = list(map(int,input().split()))

sum1, sum2 = [0]*n, [0]*n
left, right = 0, 0
for i in range(n):
    left = max(left,0) + num[i]; sum1[i] = left
    right = max(right,0) + num[~i]; sum2[~i] = right

ans = max(sum1)
for i in range(1, n-1):
    ans = max(ans, sum1[i-1]+sum2[i+1])
print(ans)