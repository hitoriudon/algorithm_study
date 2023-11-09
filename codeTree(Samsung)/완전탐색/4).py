n = int(input())
coins = [list(map(int, input().split())) for _ in range (n)]
answer = 0

for i in range (n):
    for j in range (n-2):
        answer = max(answer, sum(coins[i][j:j+3]))
print(answer)