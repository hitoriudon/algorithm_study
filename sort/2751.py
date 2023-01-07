# 2751, 수 정렬하기 2, S5

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range (N)])

for num in numbers: print(num)

# 왜 이렇게 풀었지 ㅋㅋㅋ 정답률 낮아서 괜히 딕셔너리로 시간 초과 안 나게 풀어야겠다라고 생각했는데
# 알고보니 숫자에 중복이 없어서 Counter 쓸 이유가 하나도 없었음... 걍 바보
'''
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range (N)]

numbers = Counter(sorted(numbers))

for key, value in zip(numbers.keys(), numbers.values()):
    print((str(key) + ("\n")*(value - 1)) * value)
'''
        
