from collections import deque

n = int(input())

# cals = []
queue = deque([(n, 0)])
visited = [n + 2 for _ in range (n + 2)]

ans = n + 1
while queue:
    
    current, value = queue.popleft()
    if current == 1:
        ans = min(ans, value)
        break
    
    if current % 3 == 0:
        value = min(visited[current // 3], value + 1)
        queue.append((current // 3, value))
        visited[current // 3] = value
    elif current % 2 == 0:
        value = min(visited[current // 2], value + 1)
        queue.append((current // 2, value))
        visited[current // 2] = value
    else:
        queue.append((current - 1, value + 1))
        queue.append((current + 1, value + 1))

print(ans)