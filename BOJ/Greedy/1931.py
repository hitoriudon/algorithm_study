import sys
input = sys.stdin.readline

n = int(input())
seq = sorted([tuple(map(int, input().split())) for _ in range (n)])
ans = 1
seq = sorted(seq, key = lambda x: x[1])

bx, by = seq[0]
for i in range (1, n):
    ax, ay = seq[i]
    if by <= ax:
        ans += 1
        bx, by = ax, ay
print(ans)