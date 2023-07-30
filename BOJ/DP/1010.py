# 1010, 다리 놓기, S5
# itertools combination 사용하지 않기

T = int(input())
factorial = [1, 1]
for i in range (2, 31):
    factorial.append(i * factorial[i - 1])

for _ in range (T):
    n, m = map(int, input().split())
    print(factorial[m] // (factorial[m-n] * factorial[n]))