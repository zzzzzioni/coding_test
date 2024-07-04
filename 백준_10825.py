N = int(input())

L = []
for _ in range(N):
    l = input().split()
    l[1:] = map(int, l[1:])
    L.append(l)
    
F = sorted(L, key=lambda x:x[1], reverse=True)

for    
