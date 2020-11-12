n = int(input())
signs = input().split()+['헷']

count = 0
mx = 9
mx_list = []
# 최대
for i in range(n+1):
    if len(mx_list)==(n+1):
        break
    if signs[i]=='<':
        count += 1
    else:
        x_num = mx - count - 1
        for j in range(100):
            mx_list.append(mx-count)
            if (count==0):
                mx = x_num
                break
            count -= 1
count = 0
mn = 0
mn_list = []
# 최소
for i in range(n+1):
    if len(mn_list)==(n+1):
        break
    if signs[i]=='>':
        count += 1
    else:
        n_num = mn + count + 1
        for j in range(100):
            mn_list.append(mn+count)
            if count==0:
                mn = n_num
                break
            count -= 1


## RESULTS
print(''.join(map(str, mx_list)))
print(''.join(map(str, mn_list)))