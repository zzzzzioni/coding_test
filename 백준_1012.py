# from collections import deque
import sys

# RecursionError 해결
sys.setrecursionlimit(10**6)
N = int(input())

def dfs(graph, v, d, l):
    d[v] = True
    for i in graph[v]:
        if not d[l.index(i)]:
            dfs(graph, l.index(i), d, l)      
            
for _ in range(N):
    W = []
    C = list(map(int, input().split()))
    for _ in range(C[-1]):
        W.append(list(map(int, input().split())))
    
    G = [ [] for _ in range(len(W))]
    for i in range(len(W)):
        for j in W:
            if abs(W[i][0] - j[0]) + abs(W[i][1] - j[1]) == 1:
                G[i].append(j)
    
    D = [False for _ in range(len(W))]
    
    c = 0
    for w in range(len(W)):
        if not D[w]:
            dfs(G, w, D, W) 
            c += 1
        else:
            pass
   
    print(c)
