N = int(float(input()))
C = int(input())

L = []
for _ in range(C):
    L.append(list(map(int, input().split())))
    
V = []
for l in L:
    if (l[0] == 1) & (l[1] not in V):
        V.append(l[1])
    elif (l[1] == 1) & (l[0] not in V):
        V.append(l[0])
    else:
        pass

for v in V:
    for l in L:
        if (l[0] == v) & (l[1] not in V):
            V.append(l[1])
        elif (l[1] == v) & (l[0] not in V):
            V.append(l[0])
        else:
            pass

if 1 in V:
    V.remove(1) 
    
print(len(V))