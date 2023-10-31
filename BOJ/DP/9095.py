
def solution(n, computers):
    visited=[0 for _ in range(n)]
    answer=0
    def dfs(v,visited):
        visited[v]=1
        if 0 not in visited:
            return 
        for i in range(n):
            if v!=i and computers[v][i]==1 and visited[i]==0:
                dfs(i,visited)
                print(computers)
                
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                dfs(j,visited)
                answer+=1
                
    return answer

c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3, c))

import sys
sys.setrecursionlimit(10**7)
def solution(n, computers):
    
    def dfs(v,visited):
        visited[v]=1
        for i in range(n):
            if v!=i and computers[v][i]==1 and visited[i]==0:
                dfs(i,visited)
        return visited
                

    visited=[0 for _ in range(n)]
    answer=0
                
    for i in range(n):
        if computers[i].count(1)==1:
                answer+=1
                continue
        for j in range(n):
            if i!=j and computers[i][j]==1 and visited[i]==0:
                visited=dfs(j,visited)
                answer+=1
                
    return answer
            