import sys
input=sys.stdin.readline

""" 
문장을 입력받아서, 단어들을 뒤집어서 출력함. 

- w[::-1]
"""

N=int(input())

for i in range(N):
  line=input()
  words=line.split()

  reverse_words=[]
  for w in words:
    w=w[::-1]
    reverse_words.append(w)

  print(" ".join(reverse_words))