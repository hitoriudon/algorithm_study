# 14890, 경사로, G3, 구현
N, L = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range (N)]
ans = 0
# 가로 먼저
for i in range (N):
    line = grid[i]
    stair = [False for _ in range (N)] # 경사로가 설치되어 있는지
    flag = True
    skip_cnt = 0
    for j in range (N-1):
        if skip_cnt > 0: # 경사로가 설치된 곳이면, 스킵해야 한다
            skip_cnt -= 1
            continue 
        
        if line[j] == line[j+1]: # 높이가 같아서 앞으로 전진 가능하다
            continue 
        
        elif line[j] != line[j+1]: # 높이가 다르다면, 경사로를 설치할 수 있는지 확인해야 한다
            if abs(line[j] - line[j+1]) > 1: # 경사 차이가 1보다 크면 경사로를 설치해도 지나갈 수 없다
                flag = False
                break
            
            # 현재 인덱스 j가 j+1보다 커서 내리막을 설치해야 하는데, 내리막 경사로를 설치할 수 있는 범위를 안 벗어나면서
            # 설치해야 하는 인덱스에 경사로가 설치되어 있지 않은 경우
            if line[j] > line[j+1] and j <= N - L and stair[j+1: j+1+L] == [False] * L and max(line[j+1: j+1+L]) == min(line[j+1: j+1+L]):
                for k in range (j+1, j+1+L): # 경사로 설치
                    stair[k] = True
                    skip_cnt = L - 1
                continue
            
            # 현재 인덱스 j가 j+1보다 작아서 오르막을 설치해야 하는데, 오르막 경사로를 설치할 수 있는 범위를 안 벗어나면서
            # 설치해야 하는 인덱스에 경사로가 설치되어 있지 않은 경우
            elif line[j] < line[j+1] and j >= L - 1 and stair[j+1-L: j+1] == [False] * L and max(line[j+1-L: j+1]) == min(line[j+1-L: j+1]):
                for k in range (j+1-L, j+1):
                    stair[k] = True
                continue
            
            else:
                flag = False
                break
    if flag:
        ans += 1

# 세로
for i in range (N):
    line = [grid[j][i] for j in range (N)]
    stair = [False for _ in range (N)]
    flag = True
    skip_cnt = 0
    for j in range (N-1):
        if skip_cnt > 0: # 경사로가 설치된 곳이면, 스킵해야 한다
            skip_cnt -= 1
            continue 
        
        if line[j] == line[j+1]:
            continue
        
        elif line[j] != line[j+1]:
            if abs(line[j] - line[j+1]) > 1:
                flag = False
                break
            
            # 현재 인덱스 j가 j+1보다 커서 내리막을 설치해야 하는데, 내리막 경사로를 설치할 수 있는 범위를 안 벗어나면서
            # 설치해야 하는 인덱스에 경사로가 설치되어 있지 않은 경우
            if line[j] > line[j+1] and j <= N - L and stair[j+1: j+1+L] == [False] * L and max(line[j+1: j+1+L]) == min(line[j+1: j+1+L]):
                for k in range (j+1, j+1+L): # 경사로 설치
                    stair[k] = True
                skip_cnt = L - 1
                continue
            
            # 현재 인덱스 j가 j+1보다 작아서 오르막을 설치해야 하는데, 오르막 경사로를 설치할 수 있는 범위를 안 벗어나면서
            # 설치해야 하는 인덱스에 경사로가 설치되어 있지 않은 경우
            elif line[j] < line[j+1] and j >= L - 1 and stair[j+1-L: j+1] == [False] * L and max(line[j+1-L: j+1]) == min(line[j+1-L: j+1]):
                for k in range (j+1-L, j+1):
                    stair[k] = True
                continue
            
            else:
                flag = False
                break
    if flag:
        ans += 1          

print(ans)