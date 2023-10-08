# 1946, 신입 사원, S1, 시간 초과
import sys
input = sys.stdin.readline

testcase = int(input())

for _ in range (testcase):
    n = int(input())
    people = sorted([tuple(map(int, input().split())) for _ in range (n)])
    ans = n # 빼는 방식으로

    for i in range (1, n):
        rank1, rank2 = people[i]
        for j in range (i - 1, -1, -1):
            compare_rank1, compare_rank2 = people[j]
            if rank1 > compare_rank1 and rank2 > compare_rank2:
                ans -= 1
                break
    
    print(ans)