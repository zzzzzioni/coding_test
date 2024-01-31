L = []
for _ in range(36):
    L.append(input())

A = True
B = False
C = False 

while A:    
    if len(set(L)) != 36:
        print('Invalid')
        break
    else:
        B = True
        break

F = []
for l in L:
    l = list(l)
    if l[0] == 'A':
        l[0] = 1
    elif l[0] == 'B':
        l[0] = 2
    elif l[0] == 'C':
        l[0] = 3        
    elif l[0] == 'D':
        l[0] = 4
    elif l[0] == 'E':
        l[0] = 5
    else:
        l[0] = 6
    F.append((l[0], int(l[1])))

n = 0

while B:
    for i in range(35):
        if (F[i][0] - F[i+1][0])**2 + (F[i][1] - F[i+1][1])**2 == 5:
            n += 1
        else:
            print('Invalid')
            break
    
    break

if n == 35:
    C = True 

while C:
    if (F[0][0] - F[35][0])**2 + (F[0][1] - F[35][1])**2 == 5:
        print('Valid')
        break
    else:
        print('Invalid')
        break