# 1057, 토너먼트, S4, 2트
import math
n, jm, hs = map(int, input().split())

round = 0
while jm != hs:
    jm, hs = math.ceil(jm / 2), math.ceil(hs / 2)
    round += 1
print(round)