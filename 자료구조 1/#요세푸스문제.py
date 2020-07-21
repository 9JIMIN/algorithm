N, K = map(int, input().split())
number_list = list(range(1, N+1))
answer = []
index = 0

for i in range(N):
    index += K-1
    index %= N
    answer.append( str(number_list.pop(index)) )
    N -= 1
    
print(f'<{", ".join(answer)}>')