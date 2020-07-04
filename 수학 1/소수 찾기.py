# n = int(input())
# s = list(map(int, input().split()))

# count = 0
# for i in range(n):
#     a = True
#     c = 2
#     while c-1 < s[i]//2:
#         if s[i] % c == 0:
#             a = False    
#             break
#         c += 1
#     if a and s[i] != 1: count += 1
# print(count)

"""
2

- sum([1, 2, 3]) -> 6 //리스트의 합
- all([]), all([1,2,3])= True, all([0, 1, 2])= False // 리스트를 받아서, 0이 있으면 False를 리턴
- 첫번째 인풋은 무시, 두번째 인풋을 리스트, 그걸로 루프
- 리스트 요소 n에 대하여, all(n%j for j in range(2, n))*n > 1
- sum([True, False, True..]) - True의 수를 셈. 
 """
input()
print(sum(all(n%j for j in range(2,n))*n>1 for n in map(int,input().split())))