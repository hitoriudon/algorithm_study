from collections import deque
n, k = map(int, input().split())
power = list(map(int, input().split()))
belt = deque()
for i in range (2 * n):
    belt.append([power[i], 0])

t = 1
while True:
    belt.rotate(1)
    if belt[n - 1][1] == 1: # 즉시 내려야 함
        belt[n - 1][1] = 0
        
    for i in range (n - 2, -1, -1):
        # 로봇이 있고 다음 칸 belt 내구도가 아직 있고 다음 칸에 로봇이 없다면
        if belt[i][1] != 0 and belt[i + 1][0] > 0 and belt[i + 1][1] == 0: 
            # 이동
            belt[i][1], belt[i + 1][1] = belt[i + 1][1], belt[i][1]
            # 내구도 감소            
            belt[i + 1][0] -= 1
    
    if belt[n - 1][1] == 1: # 내리는 칸에서 내리기
        belt[n - 1][1] = 0
    
    if belt[0][0] > 0: # 올리는 칸의 내구도가 1 이상이라면
        belt[0][1] = 1 # 로봇 올리기
        belt[0][0] -= 1 # 내구도 감소
    
    cnt = 0
    for i in range (2 * n):
        if belt[i][0] <= 0:
            cnt += 1
    if cnt >= k:
        print(t)
        exit()
    t += 1