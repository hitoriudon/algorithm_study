# 1003, 피보나치 함수, S3
T = int(input())
dp = [(1,0), (0,1)]
for i in range (2, 41):
    dp.append((dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]))

for _ in range (T):
    n = int(input())
    print(dp[n][0], dp[n][1])