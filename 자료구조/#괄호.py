for i in range(int(input())):  
    c=0
    for x in input():
        if x == '(':
            c += 1
        elif x == ')':
            c -= 1
        if c < 0:
            break

    print("NO"if c else"YES")