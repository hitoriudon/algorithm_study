# 14501, 퇴사, S3

n = int(input())
time, pay = [], []
for _ in range (n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0] * (n + 1)

for i in range (n):
    for j in range (i + time[i], n + 1):
        if dp[j] < dp[i] + pay[i]:
            dp[j] = dp[i] + pay[i]
print(dp)
''' 
# 테케, 자체 테케 통과, 히든 실패
n = int(input())
time, pay = [0], [0]
for _ in range (n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0] * (n + 1)
flag = False
for i in range (1, n + 1):
    if (i == n and time[i] >= 2):    
        dp[i] += 0    
    elif (i == n and flag == True):
        break
    else:
        dp[i] += pay[i]
    next = time[i]
    if next + i - 1 == n:
        dp[n] = max(dp[n], dp[i])
        flag = True
    else:    
        for j in range (next + i, n + 1):
            dp[j] = max(dp[j], dp[i])
print(dp[n])

'''