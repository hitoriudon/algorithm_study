n, m, k = map(int, input().split())
bombs = [list(map(int, input().split())) for _ in range (n)]

def check(start, value, row):
    for i in range (start + 1, n):
        if value != bombs[i][row]:
            return i - 1 # i 직전까지를 리턴
    return n - 1 # 끝까지 다 같다고 리턴
        
for count in range (k + 1): # k(회전 카운트)만큼 회전하고 마지막도 진행하려고
    boom = True
    while boom:
        boom = False
        for j in range (n):
            for start_idx in range (n):
                if bombs[start_idx][j] == 0:
                    continue
                
                end_idx = check(start_idx, bombs[start_idx][j], j)
                
                if end_idx - start_idx + 1 >= m:
                    boom = True
                    for idx in range (start_idx, end_idx + 1): # 해당 인덱스 0처리
                        bombs[idx][j] = 0 
                
            temp = []
            for i in range (n):
                if bombs[i][j] != 0:
                    temp.append(bombs[i][j])
            temp = [0] * (n - len(temp)) + temp

            for i in range (n):
                bombs[i][j] = temp[i]
        
    if count != k: # rotate

        bombs = list(zip(*bombs[::-1]))
        for i in range (len(bombs)):
            bombs[i] = list(bombs[i])
        
        for j in range (n):
            temp2 = []
            for i in range (n):
                if bombs[i][j] != 0:
                    temp2.append(bombs[i][j])
            temp2 = [0] * (n - len(temp2)) + temp2

            for i in range (n):
                bombs[i][j] = temp2[i]

ans = 0
for i in range (n):
    for j in range (n):
        if bombs[i][j] != 0:
            ans += 1
print(ans)

# 만약 K번째 회전을 진행한 이후에도 터질 폭탄이 상자에 남아있다면,
# 조건에 맞는 폭탄들을 전부 터뜨리는 것을 반복한 이후에 최종적으로 상자에 남아 있는 폭탄의 수를 구해야 합니다.

# 테케 14번 틀린 이유
# 만약 터진 이후에도 같은 열에 행 기준으로 봤을 때 연속으로 M개 이상의 같은 숫자가 있는 경우가 존재한다면, 
# 터져야 할 폭탄이 없을 때 까지 조건에 맞는 폭탄들을 터뜨리는 것을 반복합니다.
# 플래그 사용해서 while 반복해야 함.