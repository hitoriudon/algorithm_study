import sys
input = sys.stdin.readline

f = input().strip('\n').split('-')
flag = False
n = 0
for w in f:
    nums = w.split('+')
    if flag == False: # 첫 값만 + 해주고 나머진 다 빼야함 -를 기준으로 나눈 거라서
        flag = True
        n += sum(list(map(int, nums)))
    else:
        n -= sum(list(map(int, nums)))
print(n)