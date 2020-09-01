e, s, m = map(int, input().split())

elist, slist, mlist = [], [], []

for i in range(1000):
    elist.append(15*i+e)
    slist.append(28*i+s)
    mlist.append(19*i+m)

for i in range(1000):
    if elist[i] in slist and elist[i] in mlist:
        print(elist[i])
        break