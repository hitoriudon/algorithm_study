import sys
input = sys.stdin.readline

n = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

best_price = price[0]
result = 0
for i in range (n-1):
    if price[i] < best_price:
        best_price = price[i]
    result += distance[i] * best_price

print(result)