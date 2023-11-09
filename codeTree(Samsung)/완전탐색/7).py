import sys
MAX_INT = sys.maxsize

n = int(input())
check_point = [tuple(map(int, input().split())) for _ in range (n)]
min_distance = MAX_INT

for i in range (1, n - 1): # 스킵할 포인트 
    tmp = 0
    recent_idx = 0
    for j in range (1, n):
        if j == i:
            continue
        else:
            tmp += abs(check_point[j][0] - check_point[recent_idx][0]) + abs(check_point[j][1] - check_point[recent_idx][1])
            recent_idx = j
    min_distance = min(min_distance, tmp)

print(min_distance)