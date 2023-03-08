from collections import deque
n, k = map(int, input().split())
q = deque([i+1 for i in range (n)])

print("<", end="")
for _ in range (n-1):
    q.rotate(-(k-1))
    print(q.popleft(), end=", ")
print(q.popleft(), end=">")