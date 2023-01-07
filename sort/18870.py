# 18870, 좌표 압축, S2

# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
indexes = sorted(list(set(X)))

X_dict = {indexes[i] : i for i in range (len(indexes))} # indexes는 이미 정렬을 한 상태여서, value 자리엔 순위가 들어가게 됨.

for x in X:
    print(X_dict[x], end=" ")

# 시간 초과
'''
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
indexes = sorted(set(X))

for x in X:
    print(indexes.index(x), end=" ")
'''

# 딕셔너리로 접근할 수 있게 하는 게 시간복잡도를 줄이는 키 포인트.
# index()의 시간복잡도가 O(n)이라서, 시간초과가 났던 것 같다.