N = int(input())
L = []
for i in range(N):
    l = input().split()
    L.append([l[0], tuple(map(int, l[1:]))])
             

F = [[] for _ in range(366)]
D = []

for l in L:    
    for f in F[l[1][0]-1:l[1][1]]:
        f.extend(l[0])
    
    D.append(l[1][1]-l[1][0])  

i = 0
v = 0
m = 0
n = 0

for f in F:
    if len(f) > 0:
        n += 1
    if len(f) > m:
        m = len(f)
    if (f.count('S')!=0) & (f.count('S')==f.count('T')):
        i += 1
        if len(f) > v:
            v = len(f)
        else:
            pass
    else:
        pass
        

D.sort(reverse=True)

print(n)
print(m)
print(i)
print(v)
print(D[0]+1)