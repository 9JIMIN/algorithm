""" 
-2진수

입력: -13
출력: 110111

- 혼자 해결하지 못했다. 
- 받은 숫자를 2진수로 변환후 하나하나 읽어가면서 스택에 추가하는 방식으로 하려했다. 
- 하지만, 하나하나 읽어서는 안되고, 전체를 봐야 값을 구할 수 있었다. 

- 그래서 엑셀에 전체 -2진수 리스트를 적어가면서 규칙을 알아내려했다. 
- 알아내지 못함..

- 결국 구글링해서 답을 봤다. 
- 받은 숫자를 2로 나눠가면서 나오는 나머지를 추가하고, 나눈 몫이 0 이 될때까지 몫에 -2를 나눠가는 방법.

- 그렇다. 2진수라는 숫자규칙을 찾아가는 문제는 나누기에 해답이 있다.. 
 """
n = int(input())
ans = ""
while n != 1 and n != 0:
    n = -(-n//-2)
    ans = str(n%2) + ans
    print(n, ans)
if n == 0:
    print(0)
else:
    print("1"+ans)