n = int(input())
tmp = [int(input()) for _ in range (n)]
st = [0] * 301
for i in range (n):
    st[i + 1] = tmp[i]

dp = [0] * 301

dp[1] = st[1]
dp[2] = st[1] + st[2]
dp[3] = max(st[1] + st[3], st[2] + st[3])

for i in range (4, n + 1):
    dp[i] = max(dp[i - 3]+ st[i - 1] + st[i], dp[i - 2] + st[i])
print(dp[n])
