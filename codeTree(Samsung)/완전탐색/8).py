import sys
MAX_INT = sys.maxsize

n = int(input())
people = [int(input()) for _ in range (n)]

min_distance = MAX_INT

for i in range (n): # 첫번째부터 완전탐색
    dist = 0
    for j in range (n): # 순환 인덱스
        dist += people[(i+j) % n] * (j % n)
    min_distance = min(min_distance, dist)

print(min_distance)