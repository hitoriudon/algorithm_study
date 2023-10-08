# 1946, 신입 사원, S1
import sys
input = sys.stdin.readline

testcase = int(input())
answer = []
for _ in range (testcase):
    n = int(input())
    people = sorted([tuple(map(int, input().split())) for _ in range (n)]) # 서류 순위에 대해 정렬 (둘 중 먼저 오는 값)
    ans = n # 빼는 방식으로 
    top = 0
    for i in range (1, n):
        better, compare = people[top][1], people[i][1]
        if compare > better:
            ans -= 1
        # 추가해야 정답
        else:
            top = i
    answer.append(ans)

for rank in answer:
    print(rank)