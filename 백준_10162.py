T = int(input())
O = T 
A = 300
B = 60
C = 10
a = T//A
if a==0:
    b = T//B
else:
    T = T - A*a
    b = T//B
if b==0:
    c = T//C
else:
    T = T - B*b
    c = T//C
if a*A + b*B + c*C == O:
    print(a, b, c)
else:
    print(-1)