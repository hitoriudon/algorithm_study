import sys
from collections import deque
n, k = map(int, input().split())

graph = [(0, 1, 0)]
visited = [False for _ in range (k+1)]
for i in range (1, k + 1):
    graph.append((i-1, i+1, i*2))

def bfs(node):
    q = deque([graph[node]])
    visited[n] = True
    
    time = 0
    cnt = 0
    while True:
        x, y, z = q.popleft()
        
        