n = int(input())
coins = [list(map(int, input().split())) for _ in range (n)]

max_coins = 0
def idx_range(x):
    return x + 1 < n and x + 2 < n

for i in range (n): 
    for j in range (n - 2):
        for k in range (i, n):
            if k == i and n < 6:
                continue
            else:
                for l in range (j, n):
                    if (i, j) == (k, l) or (i, j+1) == (k, l) or (i, j+2) == (k, l):
                        continue
                    elif idx_range(l):    
                        coin_count = coins[i][j] + coins[i][j+1] + coins[i][j+2] + coins[k][l] + coins[k][l+1] + coins[k][l+2]
                        if max_coins < coin_count:
                            max_coins = max(max_coins, coin_count)
                            
print(max_coins)