from collections import deque

belt = deque()

n, t = map(int, input().split())
for _ in range (3):
    temp = list(map(int, input().split()))
    for num in temp:
        belt.append(num)

belt.rotate(t)

for i in range (n * 3):
    print(belt[i], end=" ")
    if (i + 1) % n == 0:
        print()