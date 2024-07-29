N, M = map(int, input().split(' '))

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(graph, i, j):
    if i < 0 or j < 0 or i >= N or j >= M:
        return False 
    
    if graph[i][j] ==  0:
        graph[i][j] = 1
        dfs(graph, i-1, j)
        dfs(graph, i, j-1)
        dfs(graph, i+1, j)
        dfs(graph, i, j+1)
        return True
    
    else:
        return False        

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += dfs(graph, i, j)
        
print(cnt)