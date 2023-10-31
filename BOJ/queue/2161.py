from collections import deque

n = int(input())

que = deque([i + 1 for i in range (n)])

while len(que):
    print(que.popleft(), end=" ")
    que.rotate(-1)