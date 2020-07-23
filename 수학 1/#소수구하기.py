# import math 

# def isPrime(num): 
#     if num == 1: return False

#     n = int(math.sqrt(num)) 
#     for k in range(2, n+1): 
#         if num % k == 0: return False 
#     return True

# m, n = map(int, input().split()) 
# for k in range(m, n+1): 
#     if isPrime(k): print(k)

""" 
2

에라토스테네스의 체로 효율적으로 소수구하기
 """

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
 
    # n을 만들기위해서 두 수를 곱할때 작은 쪽의 수는 sqrt(n)보다 항상 작음
    # 그래서 sqrt(n)까지의 숫자들만 목록에서 제거하면 됨.
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
 
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

n = int(input())
print(prime_list(n))
