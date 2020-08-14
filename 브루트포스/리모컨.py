n, m = int(input()), int(input())

no_num = abs(n-100)
if m == 0: 
    print(min(no_num,len(str(n))))
elif m == 10: 
    print(no_num)
else :
	broken = set(input().split())
	mini = 500000
	
	for i in range(1000000):
		if set(str(i)) & broken == set():
			candidate = abs(n-i) + len(str(i))
			if candidate <= mini:
				mini = candidate
	print(min(mini,no_num))