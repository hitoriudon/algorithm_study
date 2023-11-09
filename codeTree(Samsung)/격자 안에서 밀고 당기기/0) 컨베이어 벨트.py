from collections import deque

n, t = map(int, input().split()) 
belt = deque()
for _ in range (2):
    line = list(map(int, input().split()))
    for l in line:
        belt.append(l)
belt.rotate(t) 

for i in range (len(belt)):
    if i == n:
        print()
    print(belt[i], end=" ")