from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, v, visited):
    deq = deque([v])
    visited[v] = True
    while deq:
        i = deq.popleft()
        print(i, end=' ')
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True 
                deq.append(j)

        
I = list(map(int, input().split()))

L = []
for _ in range(I[1]):
    L.append(list(map(int, input().split())))

graph = [ [] for _ in range(I[0] + 1)]

for l in L:
    for i in range(1, I[0] + 1):
        if l[0] == i:
            graph[i].append(l[1])
        elif l[1] == i:
            graph[i].append(l[0])
            
for g in graph:
    g.sort()
            
visited_dfs = [False for _ in range(I[0] + 1)]
visited_bfs = [False for _ in range(I[0] + 1)]

DFS(graph, I[2], visited_dfs)
print('')
BFS(graph, I[2], visited_bfs)