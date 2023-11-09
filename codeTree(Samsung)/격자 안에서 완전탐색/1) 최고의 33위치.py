n = int(input())
coins = [list(map(int, input().split())) for _ in range (n)]
max_num = 0

for i in range (n-2):
    for j in range (n-2):
        coin_sum = 0
        for k in range (3):
            for l in range (3):
                coin_sum += coins[i+k][j+l]
        max_num = max(max_num, coin_sum)

print(max_num)