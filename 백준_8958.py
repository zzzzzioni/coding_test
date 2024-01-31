N = int(input())
L = []
for _ in range(N):
    L.append(list(input()))

for l in L:
    i = 0
    v = 0
    for e in l:
        if e=='O':
            i += 1 + v
            v += 1
        else:
            i += 0
            v = 0 
    print(i)