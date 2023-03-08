import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = set([input() for _ in range (n)])
answer = 0
for _ in range (m):
    word = input()
    if word in S:
        answer += 1
print(answer)

# 시간초과. words를 미리 만들어 놓고 탐색을 진행하니까 문제였음...
'''
S = set([(input()) for _ in range (n)])
words = [input() for _ in range (m)]
answer = 0
for s in S:
    for word in words:
        if s in words:
            answer += 1
            break
print(answer)
'''