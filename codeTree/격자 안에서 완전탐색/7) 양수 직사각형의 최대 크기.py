import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range (n)]

def check_positive(x1, y1, x2, y2):
    cnt = 0
    for i in range (x1, x2 + 1):
        for j in range (y1, y2 + 1):
            if grid[i][j] > 0 :
                cnt += 1
    
    return cnt if cnt == (x2 - x1 + 1) * (y2 - y1 + 1) else -1 # -1이면 양수 직사각형이 아니라는 뜻

max_cnt = -1 # 해당되는 사각형이 없다면 -1을 출력하라는 문제 조건에 맞게, check_positive 함수의 -1 리턴 가능성도 남겨두어야 max()로 처리하는 것에 문제가 없음
for i in range (n):
    for j in range (m):
        for k in range (i, n):
            for l in range (j, m):
                max_cnt = max(max_cnt, check_positive(i, j, k, l))
print(max_cnt)

# 17분
# 확실히 전 문제는 직사각형 두개 만들고 안 겹치게 했어야 하는데
# 이건 그냥 직사각형 하나만 두고 다 완전탐색 해보면 되니까 쉬웠음