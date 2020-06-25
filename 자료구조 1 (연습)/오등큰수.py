""" 
이것도 오큰수 비슷한데, 다른 분 답을 참고했다. 
기가 막히게 푼 답들이 많았다.
보면서 많이 배운다.

리스트의 같은 값을 세어주는 모듈
collections.Counter([1, 2, 2, 3, 3, 3]) -> Counter({3:3, 2:2, 1:1})
개수가 많은 순서대로 정렬된다.

 """

from collections import Counter

n = int(input())
arr = list(map(int,input().split()))
C = Counter(arr)
stack = []
ans = []

for x in reversed(arr):
    while stack and C[stack[-1]] <= C[x]: stack.pop()
    ans.append(stack[-1] if stack else -1)
    stack.append(x)
print(*reversed(ans))