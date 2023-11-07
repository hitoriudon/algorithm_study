from collections import deque

n, m = map(int, input().split())    
node = [[] for _ in range (n + 1)]
visited = [False for _ in range (n + 1)]
for _ in range (m):
    tx, ty = map(int, input().split())
    node[tx].append(ty)
    node[ty].append(tx)

dq = deque()
