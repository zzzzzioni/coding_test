N, M = map(int, input().split(' '))

from collections import deque

graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 상하좌우

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx < 0) or (ny < 0) or (nx >= N) or (ny >= M):
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[N-1][M-1]

print(bfs(0, 0))        

print(graph)
