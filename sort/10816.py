# 10816, 숫자 카드 2, S4

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다. 

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
my_cards = list(map(int, input().split()))
M = int(input())
your_cards = list(map(int, input().split()))

my_cards = Counter(my_cards)

for card in your_cards:
    if card in my_cards.keys():
        print(my_cards[card], end=" ")
    else: 
        print(0, end=" ")

# 배열을 딕셔너리로 변환시켜주는 Counter를 적극 활용하자.
# 바이너리 서치는 있냐 없냐 찾을 때,
# Counter는 배열에 있는 값들 개수 체크해야 할 때.


# 테케 통과, 시간 초과
'''
for i in range (N):
    c = my_cards.popleft()
    if c in your_cards:
        numbers[your_cards.index(c)] += 1
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
my_cards = deque(sorted(list(map(int, input().split()))))
M = int(input())
your_cards = deque(list(map(int, input().split())))

numbers = [0] * M # 이렇게 정답을 저장하게 되면 커지면 커질수록 시간 초과될 확률 높아진다..
for i in range (N):
    c = my_cards.popleft()
    if c in your_cards:
        numbers[your_cards.index(c)] += 1

for num in numbers:
    print(num, end=" ")
'''
