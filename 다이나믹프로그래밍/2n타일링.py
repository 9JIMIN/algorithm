
""" 
쉽고 빠르게..
 """
a,b = 1,1
for i in range(int(input())): a,b = b,a+b
print(a%10007) 

""" 
더 짧게
 """
# a=b=1;exec('a,b=b,a+b;'*int(input()));print(a%10007)