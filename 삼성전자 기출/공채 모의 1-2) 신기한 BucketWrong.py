from copy import deepcopy

n = int(input())

def is_range(x, y):
    return 0 <= x <= 3 and y >= 0

priors = [list(map(int, input().split())) for _ in range (8)]
blocks_priors = []
blocks = [tuple(map(int, input().split())) for _ in range (n)]

# 인풋을 좌표 값으로 변경 (단 좌표값은 위->아래로 쌓이는 스택이 아니라 오른->왼으로 쌓이는 스택이 기준이다)
priors_dic = {1: (0, 1), 2: (-1, 1), 3: (-1, 0), 4: (-1, -1), 5: (0, -1), 6: (1, -1), 7: (1, 0), 8: (1, 1)}
for i in range (8):
    temp = []
    for j in range (8):
        v = priors[i][j]
        # temp.append(priors_dic[(v - 3) % 8 + 1])
        temp.append(priors_dic[v])
    blocks_priors.append(temp)

ans = 0
main_stack = [[], [], [], []]
for k, c in blocks: # kind, loc
    k, c = k - 1, c - 1 # 인덱스 보정. c가 -1이면 모든 행에 다 넣어봐야 한다.
    
    # 어느 행에 넣을지 먼저 찾기
    if c == -1:
        reput = [0, 1, 2, 3] # 4번 다 해보기
    else:
        reput = [c] # 한 번만 해도 됨
    
    scores = [0, 0, 0, 0]
    candidate = []
    
    for idx in reput:
        stack = deepcopy(main_stack)
        # 블록 쌓기
        stack[idx].append(k) # 그 위치에 그냥 넣으면 됨
        
        # k를 blocks_priors 인덱스로 사용하여 우선순위 탐색을 진행.
        # 우선순위 첫번째를 적용했는데 is_range()가 안 되면 우선순위 두번째 적용하고, 안 되면 세번째... 네번째...
        max_len = 0
        for line in stack:
            max_len = max(max_len, len(line))
        
        temp_stack = [[[] for _ in range (max_len + 1)] for _ in range (4)]
        
        # 이동
        for x in range (len(stack)):
            for y in range (len(stack[x])):
                if 0 <= stack[x][y] <= 7:
                    for dx, dy in blocks_priors[stack[x][y]]:
                        nx, ny = x + dx, y + dy
                        if is_range(nx, ny):
                            temp_stack[nx][ny].append(stack[x][y])
                            break # 우선 순위대로 하면 되니까            

        # 중복 제거
        for x in range (len(temp_stack)):
            for y in range (len(temp_stack[x])):
                if len(temp_stack[x][y]) > 1: # 여러 개 있으면, 가장 작은 값만 남겨놔야 함.
                    temp_stack[x][y] = [min(temp_stack[x][y])]
        
        # 중력 적용
        new_stack = [[], [], [], []] 
        for i in range (len(temp_stack)):
            for j in range (len(temp_stack[i])):
                if len(temp_stack[i][j]) >= 1:
                    new_stack[i].append(temp_stack[i][j][0])
        stack = deepcopy(new_stack)
        
        # 폭발하며 점수 얻기
        min_len = 101
        for i in range (4):
            min_len = min(min_len, len(stack[i])) # 우선 최소 길이부터. 0이면 폭발하면 안 되고, 1이면 하나씩 터뜨려도 돼
        
        for i in range (4):
            for j in range (min_len):
                stack[i][j] = -1 # 지워버렸으
        
        # 다시 중력 적용 (값이 -1인 건 날리자)
        new_stack = [[], [], [], []]
        for i in range(len(stack)):
            for j in range (len(stack[i])):
                if stack[i][j] != -1:
                    new_stack[i].append(stack[i][j])
        stack = deepcopy(new_stack)
        scores[idx] += min_len
        candidate.append(stack) 
    choice = scores.index(max(scores))
    ans += scores[choice]
    
    if c == -1:    
        main_stack = deepcopy(candidate[choice])
    else:
        main_stack = deepcopy(candidate[0])
print(ans)
# 11
# 6 1 2 3 4 5 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 2 1
# 2 2
# 2 3
# 2 1
# 2 2
# 2 3
# 2 1
# 2 2
# 2 3
# 1 2
# 2 0