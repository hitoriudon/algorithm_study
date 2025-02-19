from collections import deque
import sys

def makeCombination(start, end, voter1):
    if len(voter1) > 0:
        f(voter1[:])

    for i in range(start, end + 1):
        voter1.append(i)  
        makeCombination(i + 1, end, voter1)  
        voter1.pop()  

def f(voter1):
    global ans
    
    voter2 = []
    for i in range (1, n + 1):
        if not i in voter1:
            voter2.append(i)
    isConnected1 = bfs(voter1)
    isConnected2 = bfs(voter2)
    
    if (isConnected1 and isConnected2): # 인구 체크
        population1, population2 = 0, 0
        
        for v in voter1:
            population1 += people[v]
        for v in voter2:
            population2 += people[v]
        
        ans = min(ans, abs(population1 - population2))
    
def bfs(voter):
    if not voter:
        return False  # 빈 선거구는 연결될 수 없음

    queue = deque([voter[0]]) 
    visited = [False] * (n + 1)
    visited[voter[0]] = True 
    count = 1 

    while queue:
        node = queue.popleft()
        for neighbor in nodes[node]: 
            if not visited[neighbor] and neighbor in voter: 
                visited[neighbor] = True 
                queue.append(neighbor)
                count += 1

    return count == len(voter)  # 방문한 노드 개수가 선거구 크기와 같으면 True, 아니면 연결 안 된 것


ans = sys.maxsize
n = int(input())
people = list(map(int, input().split()))
people = [0] + people # 인덱싱 맞춰주기 위해 인덱스 0에 0
nodes = [[]] # 인덱싱 맞춰주기 위해 인덱스 0에 빈 배열
for _ in range (n):
    temp = list(map(int, input().split()))
    for i in range (1):
        nodes.append(temp[1:])
makeCombination(1, n, [])
print(ans if ans != sys.maxsize else -1)