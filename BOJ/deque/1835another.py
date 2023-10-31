from collections import deque

n = int(input())
que = deque([i + 1 for i in range (n)])

i = 1
while len(que):
    que.rotate(-i)
    print(que.popleft(), end= " ")
    i += 1
    