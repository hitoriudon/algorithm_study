# 1920, 수 찾기, S4

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

A.sort()
if N < M:
    for a in A:
        start, end = 0, N-1
        if a > X[end] or a < X[0]:
            print(0)
        else:
            while start <= end:
                mid = (start+end) // 2 
                if a == X[mid]:
                    print(1)
                    break
                elif a < X[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # while 조건식인 start <= end가 False가 되었을 때 catch하는 역할
                print(0)
    for i in range (M-N): print(1 if X[N+i] in A else 0)
    
else:
    for x in X:
        start, end = 0, M-1    
        if x > A[end] or x < A[0]:
            print(0)
        else:
            while start <= end:
                mid = (start+end) // 2 
                if x == A[mid]:
                    print(1)
                    break
                elif x < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # while 조건식인 start <= end가 False가 되었을 때 catch하는 역할
                print(0)

'''
for x in X:
    print(1 if x in A else 0)
'''

# 파이썬 한정 베스트 풀이인 것 같다
'''
import sys

input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

for i in X: 
    if i in A:
        print(1)
    else:
        print(0)
'''