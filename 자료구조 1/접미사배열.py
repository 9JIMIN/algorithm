""" 
입력: baekjoon
출력:
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon

모든 접미사를 알파벳순으로 정렬후 출력


arr = [1,2,3]
for i in arr:
    arr.pop()
- arr가 반복문 안에서 줄어들면 반복횟수도 줄어듬.


 """

S = list(input())

arr = []
for i in range(len(S)):
    arr.append(''.join(S))
    S.pop(0)

arr = sorted(arr)
for i in arr:
    print(i)
    
""" 
개선판

- 굳이 pop을 쓰지않고 함.
- [ something for i in range() ]
- 이런식으로 for로 리스트를 만들 수 있음.
 """
s = input()
print('\n'.join(sorted([s[i:] for i in range(len(s))])))