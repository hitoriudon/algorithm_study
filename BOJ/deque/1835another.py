from collections import deque

n = int(input())
dq = deque()

dq.append(n)

for i in range (n - 1, 0, -1):
    dq.appendleft(i)
    dq.rotate(i)
    
print(*dq)