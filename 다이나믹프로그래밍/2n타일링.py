""" 
입력: 4 // 2*4타일
출력: 5 // 나열가능 경우

쭉 나열하다보면 n은 n-1, n-2의 합이라는 규칙이 보임.
 """
N = int(input())

arr=[]
for i in range(1, 1001):
    if i in [1, 2]: arr.append(i)
    else: arr.append(arr[i-2]+arr[i-3])

print(arr[N-1]%10007)

""" 
쉽고 빠르게..
 """
n = int(input())
a,b = 1,1
for i in range(n): a,b = b,a+b
print(a%10007) 

""" 
더 짧게
 """
a=b=1;exec('a,b=b,a+b;'*int(input()));print(a%10007)