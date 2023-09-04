# 14889, 스타트와 링크, S2
from itertools import combinations
import sys
MAX_INT = sys.maxsize
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range (n)]

combi = list(combinations(list(range(0, n)), n//2))
start_link = []
for i in range (len(combi) // 2):
    start_link.append([combi[i], combi[-(i+1)]])

diff = MAX_INT
for start, link in start_link:
    start_sum, link_sum = 0, 0
    for i in range (n//2):
        for j in range (i+1, n//2):
            s1, s2 = start[i], start[j]
            l1, l2 = link[i], link[j]
            start_sum += graph[s1][s2] + graph[s2][s1]
            link_sum += graph[l1][l2] + graph[l2][l1]
    diff = min(diff, abs(start_sum - link_sum))

print(diff)

# 완전탐색로 풀었음
# 짝지어야 하는 경우의 수를 combinations로 다 가지고 있는 게 효율적이라고 판단했음
# 특히, combinations의 리턴 배열은 맨 앞과 맨 뒤 인덱스가 서로 달라서 list1[i]와 list1[-(i+1)]을 짝지어서 새로운 배열에 저장했음.
# 그 뒤로는 그냥 그래프 완전 탐색. 3중 반복문을 사용한 이유는 보면 알듯