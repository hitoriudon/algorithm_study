# 2798, 블랙잭, B2

# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 
# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 
# 블랙잭은 카지노마다 다양한 규정이 있다.
# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 
# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# import sys
# from itertools import combinations
# input = sys.stdin.readline

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))

# candidates = list(combinations(cards, 3)) # 조합
# totals = sorted(list(filter(lambda x: x <= M, [sum(candidates[i]) for i in range (len(candidates))])) )

# print(totals[-1])

# 우선 candidates라는 배열에 조합 경우의 수가 다 들어있는 튜플을 생성했다.
# filter를 통해 세 카드의 합이 M보다 큰 수는 거르려고 했다. 
# filter의 첫 파라미터는 람다여야 하고, x를 좀 간편하게 할 방법 없을까? 하다가
# 두번째 파라미터는 iterable한 배열이 와야하는데, 이걸 미리 sum을 해준 상태로 넘겨주기 위해서
# 미리 튜플에 대한 sum을 다 했다. 마지막으로 이 배열을 정렬하고 -1번째 인덱스 출력해주면 끝

# itertools 사용 X

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_num = 0
for i in range (n):
    for j in range (i + 1, n):
        for k in range (j + 1, n):
            if max_num < cards[i] + cards[j] + cards[k] <= m:
                max_num = cards[i] + cards[j] + cards[k]
print(max_num)