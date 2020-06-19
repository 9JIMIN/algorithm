import sys
input=sys.stdin.readline

N=int(input())

# 데이터를 받음
input_data=[]

for n in range(N):
    el=int(input())
    input_data.append(el)


# 받은 데이터로, 아웃풋 생성
stack=[0]
output=[]
i=0
pos=True

for n in range(len(input_data)):

    if input_data[0] >= stack[0] or len(stack)==0:
        while input_data[0] != stack[0]:
            i+=1
            stack.insert(0, i)
            output.append('+')

        stack.pop(0)
        output.append('-')
    else:
        print('NO')
        pos=False
        break
    
    input_data.pop(0)

if pos==True:
    for n in output:
        print(n)