N = int(input())

P = input().split(' ')
L = []
for i in P:
    L.append(int(i))
L = sorted(L)
S = 0
for j in range(N):
    S += (N-j) * (L[j])
print(S)