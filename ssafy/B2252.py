from collections import deque

def topologySort():
    degree = [0 for _ in range (n + 1)]
    graph = [[] for _ in range (n + 1)] 

    for p1, p2 in rules:
        graph[p1].append(p2) # p1이 p2 앞에 있어야 함
        degree[p2] += 1
    
    que = deque()
    
    for i in range (1, n + 1):
        if degree[i] == 0:
            que.append(i)
    
    result = []
    while que:
        node = que.popleft()
        result.append(node)
        
        for nextNode in graph[node]:
            degree[nextNode] -= 1
            
            if degree[nextNode] == 0:
                que.append(nextNode)
    
    return result
    
n, m = map(int, input().split())
rules = [tuple(map(int, input().split())) for _ in range (m)]

ret = topologySort()

print(*ret)