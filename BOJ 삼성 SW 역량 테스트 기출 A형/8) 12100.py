# 12100, 2048(easy), G2
# L D R U 다 해보고 최대값을 기록해서 그걸 다음 grid로 확정지어야해.
# 다음 인덱스는 skip 방식으로
# row에 대한 포문이 끝났을 때 skipidx가 마지막 인덱스(길이 - 1)이 아니라면 temp에 추가해주는 방향으로
def Print():
    for line in grid:
        for num in line:
            print(num, end=" ")
        print()
    print()

import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]

for _ in range (5):
    max_num_list = []
    candidate = []
    for i in range (4): # L D R U
        temp = copy.deepcopy(grid)
        for _ in range (i): # 세팅
            temp = list(zip(*temp[::-1]))
        for k in range (len(temp)):
            temp[k] = list(temp[k])
        
        for r in range (n):
            skip_idx = -1
            temp2 = list(filter(lambda x : x > 0, temp[r]))
            temp_row = []
            for idx in range (len(temp2) - 1):
                if idx == skip_idx:
                    continue
                if temp2[idx] == temp2[idx + 1]:
                    temp_row.append(temp2[idx] + temp2[idx + 1])
                    temp2[idx + 1] = 0
                    skip_idx = idx + 1
                else:
                    temp_row.append(temp2[idx])
            if skip_idx != len(temp2) - 1:
                temp_row.append(temp2[-1])
            
            temp_row += [0] * (n - len(temp_row))
            
            for j in range (n):
                temp[r][j] = temp_row[j]
        
        for _ in range (4 - i): # 돌려놓기
            temp = list(zip(*temp[::-1]))
        for k in range (len(temp)):
            temp[k] = list(temp[k])
        
        candidate.append(temp)
        
        temp_max_num = 0
        for line in temp:
            temp_max_num = max(temp_max_num, max(line))
        temp_max_num_cnt = 0
        for line in temp:
            temp_max_num_cnt += line.count(temp_max_num)
        max_num_list.append((temp_max_num, temp_max_num_cnt))
        
    select = max_num_list.index(max(max_num_list))
    grid = copy.deepcopy(candidate[select])
    Print()
ans = 0
for line in grid:
    ans = max(ans, max(line))
print(ans)