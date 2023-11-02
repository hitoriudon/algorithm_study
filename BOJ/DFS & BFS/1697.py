# 1697, 숨바꼭질, S1, 2트

from collections import deque

begin, end = map(int, input().split())
queue = deque()   
visited = [False for _ in range (100001 * 2)]
queue.append((begin, 0))

while True:
    curr, time = queue.popleft()
    if curr == end:
        print(time)
        exit()
    
    if not visited[curr - 1] and curr > 0:    
        queue.append((curr - 1, time + 1))
        visited[curr - 1] = True

    if not visited[curr + 1] and curr + 1 < 100001:
        queue.append((curr + 1, time + 1))
        visited[curr + 1] = True

    if not visited[curr * 2] and curr * 2 < 100001 :
        queue.append((curr * 2, time + 1))
        visited[curr + 1] = True

# 메모리 초과났던 건 visited 처리랑 curr 범위 처리를 안 했음