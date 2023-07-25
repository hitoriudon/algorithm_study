# 1026, 보물, S4

# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
# N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

# 첫째 줄에 S의 최솟값을 출력한다.

from collections import deque

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_copy , B_copy = deque(sorted(A)), deque(sorted(B)) # list의 pop()은 O(n), deque의 popleft()는 O(1)라서 빨리 하려고.. 시간 제한 2초라서
B_copy.reverse()

result = 0
new_A = [0] * N
for i in range (N):
    a = A_copy.popleft()
    b = B_copy.popleft()
    result += a * b
    # 추가) A 배열 위치 바꾸기
    x = A.index(a) 
    y = B.index(b)
    new_A[y] = A[x]
print(result)
# 추가) A 배열 출력
print(new_A)