N = int(input())

rope = []

for i in range(N):
    rope.append(int(input()))

# 정렬하고,
rope.sort()
# 작은 로프까지 사용했을 때 들 수 있는 최대 하중 계산 
for i, r in enumerate(rope):
    rope[i] = r * (N-i)
# 최대 하중 출력 
print(max(rope))
