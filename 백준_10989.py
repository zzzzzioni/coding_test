# N = int(input())

# L = []
# for _ in range(N):
#     L.append(int(input()))
    
# for _ in range(N):
#     print(L.pop(L.index(min(L))))


# 질문 게시판 참고 ... 
# 빠른 입출력 
import sys

n = int(sys.stdin.readline().rstrip()) # sys는 \n도 같이 받기 때문임 
C = [0] * 10000

for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    C[i-1] += 1

for j in range(10000):
    if C[j] != 0:
        for _ in range(C[j]):
            sys.stdout.write(str(j+1)+'\n')

