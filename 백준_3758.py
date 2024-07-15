### 시간 초과 ###

N = int(input())

T = []
INFO = []
for _ in range(N):
    case = []
    info = list(map(int, input().split()))
    INFO.append(info)
    for _ in range(info[3]):
        case.append(list(map(int, input().split())))
    
    T.append(case)

# 팀 개수, 문제 개수, ID, 요소 개수 

# (문제벌 점수, 제출 횟수)
# 팀마다 [n번의 문제 최고점 기록]
for c in T:
    info = INFO[T.index(c)]
    Rank = [ [0] * (info[1]+3) for _ in range(info[0])]
    for e in c:
        # e = [팀ID, 문제ID, 점수]
        Rank[e[0]-1][e[1]-1] = max(Rank[e[0]-1][e[1]-1], e[2])
        Rank[e[0]-1][info[1]] += 1
        Rank[e[0]-1][info[1]+1] = int(c.index(e))
    
    Score = sorted(Rank, key = lambda x : (-sum(x[:info[1]]), x[info[1]], x[info[1]+1]))
    
    index = next((i for i, sublist in enumerate(Score) if sublist[0] == info[2]), -1)
    print(index+1)
