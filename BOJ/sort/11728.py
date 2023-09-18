import sys
input = sys.stdin.readline
n, m = map(int, input().split())

nlist = list(map(int, input().split()))
mlist = list(map(int, input().split()))

result = nlist + mlist

for num in sorted(result):
    print(num, end=" ")