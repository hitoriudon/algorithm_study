n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range (n)]

p = 0
for i in range (n):
    r, c = 0, 0
    cnt1, cnt2 = 0, 0
    for j in range (n-1): # 가로 체크 nums[i][j]
        if nums[i][j] == nums[i][j+1]: # 연속 카운팅
            r += 1
            cnt1 = max(cnt1, r)
        elif nums[i][j] != nums[i][j+1]: # 초기화
            r = 0 
    if cnt1 >= m - 1:
        p += 1            
        
    for j in range (n-1): # 세로 체크 nums[j][i]
        if nums[j][i] == nums[j+1][i]:
            c += 1
            cnt2 = max(cnt2, c)
        elif nums[j][i] != nums[j+1][i]:
            c = 0
    if cnt2 >= m - 1:
        p += 1
        
print(p)