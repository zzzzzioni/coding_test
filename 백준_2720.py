T = int(input())

def cal(T):
    Q = 25
    D = 10
    N = 5
    P = 1

    if T//Q == 0:
        q = T//Q
    else:
        q = T//Q
        T = T - Q*q
    if T//D == 0:
        d = T//D
    else: 
        d = T//D
        T = T - D*d
    if T//N == 0:
        n = T//N
    else:
        n = T//N
        T = T - N*n
    print(q, d, n, T)
    
for _ in range(T):
    C = int(input())
    cal(C)