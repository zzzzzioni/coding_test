from itertools import combinations

N = list(map(int, input().split()))

L = []
for _ in range(N[0]):
    L.append(list(map(int, input().split())))

H = []
C = []
for i in range(N[0]):
    for j in range(N[0]):
        if L[i][j] == 1:
            H.append((i+1, j+1))
        elif L[i][j] == 2:
            C.append((i+1, j+1))
        else:
            pass


best = []
final = 0

comb = list(combinations(C, N[1]))

for i in comb:
    final = 0
    for h in H:
        final_d = N[0]**2
        for c in i:
            if (abs(h[0]-c[0]) + abs(h[1]-c[1])) < final_d:
                final_d = (abs(h[0]-c[0]) + abs(h[1]-c[1]))
            else:
                pass
        
        final += final_d
    best.append(final)

best.sort()
print(best[0])

    