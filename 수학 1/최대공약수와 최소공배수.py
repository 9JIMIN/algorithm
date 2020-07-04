""" 
입력: 18 24
출력: 
6 
72

- map은 map형식을 리턴하기에 list(map()) 이렇게 다시 list로 만들어줘야함. 
- 근데 a, b = map() 이런식으로하면 list로 감쌀 필요없음.
- 4/2= 2.0 float가 나옴. 4//2는 int가 나옴.

- a, b 의 최소공배수 = a * b / 최대공약수

- 최대공약수를 구하는 것이 관건인 문제!
- 최대공약수는 두 수를 나눈 나머지가 0 이 되도록 나눠가는 과정.
 """

a, b = map(int, input().split())
p = a * b
while a:
    a, b = b%a, a

print(b)
print(p//b)