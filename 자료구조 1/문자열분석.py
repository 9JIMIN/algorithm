""" 
문자열의 여러줄을 받아서// 소문자, 대문자, 숫자, 공백의 개수를 출력

입력: 
This is String
SPACE    1    SPACE
 S a M p L e I n P u T     
0L1A2S3T4L5I6N7E8

출력: 
10 2 0 2
0 10 1 8
5 6 0 16
0 8 9 0

- 여러줄의 input을 받아야하는 상황
- iter(호출객체, 반복을 끝낼값) 반복하다가, 특정값이 나오면 멈춤.

- 이렇게 받는게 아니었음..
 """

n = '\n'.join(iter(input, '')).splitlines()

for i in range(len(n)):
    out = [0, 0, 0, 0]
    for c in n[i]:
        if ord(c) >= 97 and ord(c) <= 122: out[0] += 1
        elif ord(c) >= 65 and ord(c) <= 90: out[1] += 1
        elif ord(c) >= 49 and ord(c) <= 57: out[2] += 1
        elif ord(c) == 32: out[3] += 1

    print(*out)


""" 
개선판

- readline은 한줄한줄 읽을 수 있음.
- islower, isupper, isnumeric, isspace 함수의 사용.

 """
import sys

while True:
    out = [0, 0, 0, 0]
    n = sys.stdin.readline()
    if not n:
        break
    for i in n:
        if i.islower():
            out[0] += 1
        elif i.isupper():
            out[1] += 1
        elif i.isnumeric():
            out[2] += 1
        elif i == " ":
            out[3] += 1
    print(*out)