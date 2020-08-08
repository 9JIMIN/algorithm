n = int(input()) 
tile = [0] * 31 
tile[2] = 3 

for i in range(4, n+1, 2): 
    tile[i] = 2 + tile[i-2] * 3 + sum(tile[:i-2]) * 2 
print(str(tile[n]))
