# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ') # 방문하면 출력 
    for i in graph[v]:
        if not visited[i]: 
            dfs(graph, i, visited) # 인접한 노드를 먼저 방문하고, 그 노드에서 또 for문이 돌면서 인접 노드를 방문하는 구조 (깊어짐)
            

# bfs 
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue: # 빈 deque는 False
        v = queue.popleft() # queue의 첫번째 노드(가장 작은 노드)부터 빼내고, 걔의 인접 노드를 방문하고 ... 반복 
        print(v, end=' ') # 출력
        for i in graph[v]: 
            if not visited[i]:
                queue.append(i)
                visited[i] = True # 인접 노드를 모두 방문 

graph = [
    [], # index가 0부터 시작하니까! 
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
] 

visited = [False for _ in range(len(graph))]

dfs(graph, 1, visited)
bfs(graph, 1, visited)


