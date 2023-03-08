import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for i in range (1, n):
    A[i] = max(A[i], A[i-1] + A[i])
print(A)
