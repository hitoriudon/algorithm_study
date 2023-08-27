n = int(input())
coins = [list(map(int, input().split())) for _ in range (n)]

max_num = 0

for i in range (n):
    for j in range (n-2):
        for k in range (i, n):
            for l in range (n-2):
                if i == k and abs(j-l) <= 2:
                    continue
                start_coin = coins[i][j] + coins[i][j+1] + coins[i][j+2]
                target_coin = coins[k][l] + coins[k][l+1] + coins[k][l+2]
                
                max_num = max(max_num, (start_coin + target_coin))

print(max_num)