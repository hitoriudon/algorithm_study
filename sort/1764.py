# 1764, 듣보잡, S4

# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())

names = Counter(sorted([input().strip("\n") for _ in range (N+M)]))

cnt = 0
for value in names.values():
    if value == 2:
        cnt += 1
print(cnt)
for name, value in zip(names.keys(), names.values()):
    if value == 2:
        print(name)
        
# 어차피 듣 배열에도 중복이 없고, 보 배열에도 중복이 없으면
# 듣보가 되려면 합이 2라서.. 걍 두 배열을 합쳐서 Counter로 개수 셌음