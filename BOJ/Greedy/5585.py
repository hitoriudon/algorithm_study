n = int(input())
change = 1000 - n
quantity = 0

coins = [500, 100, 50, 10, 5, 1]
i = 0

while change >= 1:
    if change >= coins[i]:
        change -= coins[i]
        quantity += 1
    else:
        i += 1

print(quantity)