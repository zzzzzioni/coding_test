N = int(input())

L = []
for _ in range(N):
    T = list(map(int, input().split()))
    L.append(T)

L.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for i in range(N):
    if end <= L[i][0]:
        count += 1
        end = L[i][1]
        
print(count)
    