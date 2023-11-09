# deque 사용 X
n, time = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range (3)]

for t in range (time):
    temp = [0, 0, 0]
    for i in range (3):
        temp[(i+1) % 3] = belt[i][-1]
        for j in range (n - 1, 0, -1):
            belt[i][j] = belt[i][j-1]
        belt[i][0] = temp[i]
    belt[0][0] = temp[0]

for i in range (3):
    for j in range (n):
        print(belt[i][j], end=" ")
    print()