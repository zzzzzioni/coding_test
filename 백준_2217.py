N = int(input())

rope = []

for i in range(N):
    rope.append(int(input()))

rope.sort()

for i, r in enumerate(rope):
    rope[i] = r * (N-i)
    
print(max(rope))
