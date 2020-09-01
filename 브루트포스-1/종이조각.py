n, m = map(int,input().split())
paper = [list(map(int,input())) for i in range(n)]

def tonum(L):
    return int(''.join(map(str,L)))

def opt(L,i,j,maxi,maxj):
    if i > maxi or j > maxj:
        return 0
    best = max(tonum(L[i][j:maxj+1])+opt(L,i+1,j,maxi,maxj),
               tonum(L[maxi][j:maxj+1])+opt(L,i,j,maxi-1,maxj),
               tonum([L[z][j] for z in range(i,maxi+1)])+opt(L,i,j+1,maxi,maxj),
               tonum([L[z][maxj] for z in range(i,maxi+1)])+opt(L,i,j,maxi,maxj-1))
    return best

print(opt(paper,0,0,n-1,m-1))