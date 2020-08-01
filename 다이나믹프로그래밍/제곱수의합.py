# n = int(input())
# num = [i**2 for i in range(1, 318)]
# c = 0
# while n:
#     for i in range(317):
#         if n - num[i] < 0:
#             n = n - num[i-1]
#             c += 1
#             break
# print(c)

n = int(input())
d = [0]*(n+1)
for i in range(1, n+1):
    d[i] = min([d[i-j**2]+1 for j in range(1,int(i**0.5)+1)])
print(d[-1])