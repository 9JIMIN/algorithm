# n = int(input())
# count = 0
# length = len(str(n))
# for i in range(length):
#     count += i*(9*(10**(i-1)))
# count += length*(n-10**(length-1)+1)
# print(int(count))

n = int(input())
count, i = 0, 1
while n >= i:
    count += n - i + 1
    i *= 10
print(count)