# 12100, 2048(easy), G2
# L D R U 다 해보고 최대값을 기록해서 그걸 다음 grid로 확정지어야해. -> 틀렸음!!! 그냥 다 해봐야 해 브루트 포스로
# 다음 인덱스는 skip 방식으로
# row에 대한 포문이 끝났을 때 skipidx가 마지막 인덱스(길이 - 1)이 아니라면 temp에 추가해주는 방향으로 -> 굳이 이렇게 안 해도 됨
import copy

def Print():
    for line in grid:
        for num in line:
            print(num, end=" ")
        print()
    print()
    
def run(nums, grid):
    for num in nums:
        temp = copy.deepcopy(grid)
        for _ in range (num):
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

        for _ in range (n - num):
            temp = list(zip(*temp[::-1]))
        for k in range (len(temp)):
            temp[k] = list(temp[k])
        
        grid = copy.deepcopy(temp)      
    
    max_num = 0
    for line in grid:
        max_num = max(max_num, max(line))
    
    return max_num

n = int(input())
grid = [list(map(int, input().split())) for _ in range (n)]
ans = 0
for a in range (4):
    for b in range (4):
        for c in range (4):
            for d in range (4):
                for e in range (4):
                    seq = [a,b,c,d,e]
                    ans = max(ans, run(seq, grid))

print(ans)