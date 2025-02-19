import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(que, (0, start))
    
    while que:
        currentWeight, currentNode = heapq.heappop(que) # 우선순위가 가장 낮은 값(= 가장 작은 거리)이 pop
        
        if distance[currentNode] < currentWeight: # 이미 입력되어있는 값이 현재 노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue
        
        for connectedWeight, connectedNode in graph[currentNode]:
            dist = currentWeight + connectedWeight
            if dist < distance[connectedNode]:
                distance[connectedNode] = dist
                heapq.heappush(que, (dist, connectedNode))

n, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range (n + 1)]
for _ in range (e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distance = [INF for _ in range (n + 1)]
que = []
    
dijkstra(k)

for i in range (1, n + 1):
    print("INF" if distance[i] == INF else distance[i])
    
