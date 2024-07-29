N, L = map(int, input().split(' '))


R = []
for _ in range(N):
    R.append(list(map(int, input().split(' '))))

R_T = []
for i in range(N):
    r = []
    for j in range(N):
        r.append(R[j][i])
    R_T.append(r)


def check(lst):
    for l in lst:
        for i in range(N):
            if i == 0:
                past = l[i]
            else:
                crt = past - l[i]
                if crt == 0:
                    pass
                elif crt == 1:
                    
                else:
                    break


def check_cell(cell, i, j):
        for l in range(L):
            if (cell[i][j] == cell[i+1][j] + 1) & 
            
            elif (cell[i][j] == cell[i-1][j] + 1)
















C = [[0] * N for _ in range(N)]

def check(lst):
    for i in range(N):
        for j in range(N):
            if j == 0:
                past = (i, j)
            else:
                if C[i][i] == 0:
                    crt = past[1] - lst[i][j]
                    if crt == 0:
                        C[past[0]][past[1]] = 1
                    elif crt == 1:
                        

                    else:
                        break    
            
                else:
                    pass

def check_cell(cell, i, j):
        for l in range(L):
            if (cell[i][j] == cell[i+1][j] + 1) & 
            
            elif (cell[i][j] == cell[i-1][j] + 1)
