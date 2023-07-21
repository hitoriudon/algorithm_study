# 1193, 분수 찾기, S5
import sys
input = sys.stdin.readline
n = int(input())

# 메모리 초과
'''
integer = 0
while True:
    integer += 1
    before, after = sum(list(range(1, integer + 1))), sum(list(range(1, integer + 2)))
    if before <= n < after:
        break
n_list = [(0, 0)] # initialized idx 0
for idx in range (1, integer + 2):
    bunja, bunmo = 1, 1
    if idx % 2 == 1:
        for cnt in range (idx):
            n_list.append((bunja + (idx - 1) - cnt, bunmo + cnt))
    else:
        for cnt in range (idx):
            n_list.append((bunja + cnt, bunmo + (idx - 1) - cnt))
print(n_list)
print(len(n_list))
print(n_list[n])
'''
# 시간 초과
'''
integer = 0
while True:
    integer += 1
    before, after = sum(list(range(1, integer + 1))), sum(list(range(1, integer + 2)))
    if before <= n < after:
        break
n_list = [(0, 0)] # initialized idx 0
for idx in range (1, integer + 2):
    bunja, bunmo = 1, 1
    if idx % 2 == 1:
        for cnt in range (idx):
            n_list.pop()
            n_list.append((bunja + (idx - 1) - cnt, bunmo + cnt))
            n -= 1
            if n == 0:
                break
    else:
        for cnt in range (idx):
            n_list.pop()
            n_list.append((bunja + cnt, bunmo + (idx - 1) - cnt))
            n -= 1
            if n == 0:
                break

x, y = str(n_list[n][0]), str(n_list[n][1])
print(x + "/" + y)
'''