""" 
다른분 답 참고하였다.

- 하나하나 바로 찾는거는 n^2로 오래걸림.
- 스택에 오큰수를 못찾은 인덱스를 넣어주는 방법.
- 
"""
N = int(input())
num = [*map(int,input().split())]

stack = []
nge = [-1 for _ in range(N)]

for i in range(N):
  while stack and num[stack[-1]] < num[i]:
    nge[stack.pop()] = num[i]
  stack.append(i)
print(*nge)

"""  
아래는 stack이 비었는 경우를 에러로 받았음. 비효율적. 
리스트를 출력할 때도 for 없이, 
print(*[1, 'a', True]) *리스트는 한칸씩 띄워서 요소들을 출력할 수 있음.
"""
# numbers = int(input())
# num_list = list(map(int, input().split()))
# stack = []
# result = [-1 for _ in range(numbers)] 
# # [-1, -1, -1, ..] numbers수만큼 -1 _는 값(인덱스)를 무시한다는 뜻 

# for i in range(len(num_list)):
#     try:
#         while num_list[stack[-1]] < num_list[i]:
#             result[stack.pop()] = num_list[i]
#     except:
#         pass
#     stack.append(i)
        
# for i in range(numbers):
#     print(result[i], end = ' ')

""" 
루프 이전에 if를 넣어서 해결했다 생각했는데, 그래도 시간초과.
 """
# import sys
# input = sys.stdin.readline

# N = int(input())
# num = list(map(int, input().split()))

# answer = []

# for i in range(N):
#     s = i

#     if i > 0 and nge and num[i] <= num[i-1]:
#         answer.append(nge)
#     else:
#         while True:
#             if s > N-2:
#                 nge = -1
#                 break
#             if num[i] < num[s+1]:
#                 nge = num[s+1]
#                 break
#             nge = -1
#             s += 1
#         answer.append(nge)

# for n in answer:
#     print(n, end=' ')


""" 
처음 낸거 - 시간초과 
100개가 있고, 전부 1에 마지막에 2가 있으면, 100^100의 이중루프
"""
# import sys
# input = sys.stdin.readline

# N = int(input())
# num = list(map(int, input().split()))

# answer = []

# for i in range(N):
#     s = i
#     nge = False
#     while s < N-1:
#         if num[i] < num[s+1]:
#             nge = num[s+1]
#             break
#         s += 1
#     if nge:
#         answer.append(nge)
#     else:
#         answer.append(-1)

# for n in answer:
#     print(n, end=' ')
