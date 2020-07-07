""" 
입력: back
출력: 1 0 2 -1 -1 -1 -1 -1 -1 -1 3 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

- 단어에서 해당하는 알파벳 인덱스를 보여줌. 없는거는 -1
 """
# S = input()
# for i in range(26): 
#     if chr(i+97) in S:
#         print(S.index(chr(i+97)), end=" ")
#     else:
#         print(-1, end=" ")

""" 
개선판

- find는 없으면, -1을 출력함. ex) 'jimin'.find('a') -> -1
- map은 iter한 애들을 받아서 함수를 적용한 리스트를 리턴한다. 
- * 는 리스트를 언팩.
 """
from string import ascii_lowercase as au
print(*map(input().find, au))